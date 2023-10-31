from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI(
    title="NLP Engineer Assignment",
    version="1.0.0"
)


@app.get("/", include_in_schema=False)
async def index():
    """
    Redirects to the OpenAPI Swagger UI
    """
    return RedirectResponse(url="/docs")


# TODO: Add a route to the API that accepts a text input and uses the trained
# model to predict the number of occurrences of each letter in the text up to
# that point.
