from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()


# Define a Pydantic model for the response
class ExampleResponse(BaseModel):
    message: str


@router.get(
    "/example",
    response_model=ExampleResponse,
    status_code=status.HTTP_200_OK,
    summary="Read Example",
    description="This endpoint returns a simple example message.",
)
async def read_example():
    """
    ## Example Endpoint

    This endpoint returns a simple example message as a JSON response.

    ### Response:
    - **message**: A string that contains the message.

    ### Example Response:
    - `{"message": "This is an example endpoint"}`
    """
    return {"message": "This is an example endpoint"}
