[Back to main](../README.md)
# Room
[Add Room](#add-room)<br>
[Remove Room](#remove-room)<br>
[Get All Room Info](#get-all-room-info)<br>
[Get All Rooms](#get-all-rooms)<br>
<br><br>

# Endpoint: /Room

## Add Room
[Back to the top](#room)
### POST 
### Expected Request<br><br>
```json
{
    "body": {
        "room_name": "AB203",
        "room_length": 20,
        "room_width": 12
    },
    "action": "add_room"
}
```
### <br>

| Variable    | Data Type | Required | Additional Validation |
|-------------|-----------|----------|-----------------------|
| room_name   | string    | Yes      | No                    |
| room_width  | integer   | Yes      | No                    |
| room_length | integer   | Yes      | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Room added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Remove Room
[Back to the top](#room)
### DELETE
### Expected Request ?action=remove_room&room_id=6<br><br>
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| room_id  | integer   | Yes      | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Room removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get All Room Info
[Back to the top](#room)
### GET
### Expected Request: ?action=get_all_room_info&room_id=4<br><br>
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| room_id  | integer   | Yes      | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Json object storing information pertaining to the room"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get All Rooms
[Back to the top](#room)
### GET 
### Expected Request ?action=get_all_rooms<br><br>
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
|          |           |          |                       |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Array storing all rooms and their info"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```