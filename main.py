from fastapi import FastAPI, HTTPException, status

app=FastAPI()

shipments: dict[int, dict[str, str]] = {
    1234: {"content": "books", "status": "delivered"},
    1235: {"content": "laptop","status": "in transit"},
    1236: {"content": "desk lamp", "status": "pending"},
    1237: {"content": "coffee maker", "status": "delivered"},
    1238: {"content": "keyboard", "status": "in transit"},
    1239: {"content": "monitor stand", "status": "pending"},         
    1240: {"content": "usb cables", "status": "delivered"},
    1241: {"content": "headphones", "status": "in transit"},
    1242: {"content": "mouse pad", "status": "pending"},
    1243: {"content": "external hard drive", "status": "delivered"},
    1244: {"content": "webcam", "status": "in transit"},
    1245: {"content": "desk organizer", "status": "pending"},
    1246: {"content": "notebook set", "status": "delivered"},
    1247: {"content": "pen holder", "status": "in transit"},
    1248: {"content": "desk chair", "status": "pending"},
    1249: {"content": "monitor", "status": "delivered"},
}

@app.get("/")
def get_shipments():
    return shipments

@app.get("/shipment/latest")
def get_shipment():
    latest = max(shipments.keys())
    return {
        "id": latest,
        "status": shipments[latest]["status"],
        "content": shipments[latest]["content"]
    }

@app.get("/shipment/{id}")
def get_shipment(id: int | float):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shipment with id {id} not found"
        )
    return {
        "id": id,
        "content": shipments[id]["content"],
        "status": shipments[id]["status"]
    }

@app.post("/shipment")
def submit_shipment(content: str):
    id = max(shipments.keys()) + 1
    shipments[id] = {
        "content": content,
        "status": "placed"
    }

    return shipments.get(id)


