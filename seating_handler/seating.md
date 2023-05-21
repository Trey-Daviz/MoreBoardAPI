[Back to main](../README.md)
# Seating
[Add Chairs To Seating Arrangement](#add-chairs-to-seating-arrangement)<br>
[Remove Chairs From Seating Arrangement](#remove-chairs-from-seating-arrangement)<br>
[Get Student From Chair](#get-student-from-chair)<br>
<br><br>

# Endpoint: /Seating

## Add Chairs To Seating Arrangement
[Back to the top](#seating)
### POST
### Example Request<br><br>
```json
{
    "body": {
        "class_id": 6,
        "arrangement": [
            {
                "x": 10,
                "y": 30,
                "student_id": 8
            }
        ]
    },
    "action": "add_chair_to_seating_arrangement"
}
```
### <br>

| Variable    | Data Type        | Required | Additional Validation |
|-------------|------------------|----------|-----------------------|
| class_id    | integer          | Yes      | No                    |
| arrangement | array of objects | Yes      | No                    |

### Object inside of arrangement

| Variable   | Data Type | Required | Additional Validation |
|------------|-----------|----------|-----------------------|
| x          | integer   | Yes      | No                    |
| y          | integer   | Yes      | No                    |
| student_id | integer   | Yes      | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Chairs added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Remove Chairs From Seating Arrangement
[Back to the top](#seating)
### DELETE
### Example Request: <br>?chair_ids=[22]&action=remove_chairs_from_seating_arrangement<br><br>

| Variable  | Data Type         | Required | Additional Validation                                              |
|-----------|-------------------|----------|--------------------------------------------------------------------|
| chair_ids | array of integers | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Chairs Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get Student From Chair
[Back to the top](#seating)
### GET
### Example Request ?chair_id=19&action=get_student_from_chair
<br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| chair_id | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Student information pertaining to that chair"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```
