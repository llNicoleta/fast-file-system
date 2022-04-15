from event_model import Event
from response_model import Response, BaseResponse

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'title': 'Fast File System'}


@app.post("/events", response_model=Response)
async def add_event(event: Event) -> Response:
    # TODO: check for hash in db before returning risk_level
    return Response(file=BaseResponse(hash=event.file.file_hash, risk_level=-1),
                    process=BaseResponse(hash=event.last_access.hash, risk_level=-1))


if __name__ == '__main__':
    uvicorn.run(app)