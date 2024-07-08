"""
@author: jldupont
"""
import subprocess
from typing import List, Tuple, Any, Union
from .models import Result, Param, Params
from .utils import prepare_params, split_head_tail


class CommandLine:

    def __init__(self, exec_path: str):
        assert isinstance(exec_path, str)
        self.exec_path = exec_path
        self._last_command_args = None

    @property
    def last_command_args(self) -> List[Any]:
        return self._last_command_args

    def exec(self, params: Params, common: Params = None) -> Result:
        assert isinstance(params, list), f"Expected list, got: {type(params)}"

        if common is None:
            common = []

        command_args = prepare_params([self.exec_path] + params + common)

        try:
            result = subprocess.run(
                command_args,              # Command to execute
                stdout=subprocess.PIPE,    # Capture stdout
                stderr=subprocess.PIPE,    # Capture stderr
                text=True                  # Decode output as text
            )
        except FileNotFoundError:
            raise FileNotFoundError(f"Command not found: {self.exec_path}")
        except PermissionError:
            raise PermissionError("Permission denied (or possibly "
                                  f"invalid exec path): {self.exec_path}")

        self._last_command_args = command_args

        if result.returncode == 0:
            return Result(
                success=True,
                message=result.stdout.strip(),
                code=0
            )
        return Result(
            success=False,
            message=result.stderr.strip(),
            code=result.returncode
        )


class GCloud(CommandLine):
    """
    https://cloud.google.com/sdk/gcloud/reference

    gcloud [alpha|beta] group [subgroup] command [params]

    Examples:
    ---------
    gcloud run describe my-service
    gcloud run deploy $name
    gcloud run jobs create $name
    gcloud run jobs describe $name
    gcloud run services list
    """

    def __init__(self, *head_tail: Union[List[Union[str, Tuple[str, str]]],
                                         Param], cmd="gcloud"):
        """
        head_tail: [head_parameters ...] tail_parameters
        """
        super().__init__(cmd)
        self.head_tail = head_tail

    def __call__(self, *head_after: List[Union[str, Tuple[str, str], Param]]) \
            -> Result:
        """
        head_after: parameters that will be added at the head of the list
              following what was provided during initialization
        """
        head, tail = split_head_tail(self.head_tail)
        liste = head + list(head_after)
        liste.extend(tail)
        return self.exec(liste)


gcloud = GCloud()
