[Back to main](../README.md)
# Class
[Add Class](#add-class)<br>
[Remove Class](#remove-class)<br>
[Add User To Class](#add-user-to-class)<br>
[Remove User From Class](#remove-user-from-class)<br>
[Get All Users From Class](#get-all-users-from-class)<br>
[Get All Chairs From Class](#get-all-chairs-from-class)<br>
[Get All Classes](#get-all-classes)<br>
[Assign Teacher To Class](#assign-teacher-to-class)<br>
<br><br>


## Endpoint
### /Class


## Add Class
[Back to the top](#class)
### POST
### Expected Request<br><br>
```json
{
    "body": {
        "teacher_username": "RS600499",
        "class_name": "Test Class",
        "hour": 4,
        "room_id": 4
    },
    "action": "add_class"
}
```
### <br>

| Variable         | Data Type | Required | Additional Validation                                |
|------------------|-----------|----------|------------------------------------------------------|
| teacher_username | string    | True     | Must be a username ascribed to a teacher             |
| class_name       | string    | True     | No                                                   |
| hour             | integer   | True     | Teacher must not have other class at this hour       |
| room_id          | integer   | True     | Room must not have a class taught in it at this hour |



### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Class added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Remove Class
[Back to the top](#class)
### DELETE 
### Expected Request 
### ?class_id=7&action=remove_class<br><br>

### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| class_id | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Class Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get All Users From Class
[Back to the top](#class)
### GET
### Expected Request<br><br>?class_id=1&action=get_all_users_from_class<br>

### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| class_id | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "array of user information for that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Add User To Class
[Back to the top](#class)
### POST
### Expected Request<br><br>
```json
{
    "body": {
        "class_id": 21,
        "user_id": 71
    },
    "action": "add_user_to_class"
}
```
### <br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| class_id | integer   | True     | No                    |
| user_id  | integer   | True     | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User has been added to that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Remove User From Class
[Back to the top](#class)
### DELETE
### Expected Request
### ?class_id=2&user_id=244&action=remove_user_from_class<br><br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| class_id | integer   | True     | No                    |
| user_id  | integer   | True     | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User has been added to that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

# Get All Chairs From Class
[Back to the top](#class)
### GET
### Expected Request<br><br>?class_id=1&action=get_all_chairs_from_class<br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| class_id | integer   | True     | No                    |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "array with all chairs in the provided class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get All Classes
[Back to the top](#class)
### GET
### Expected Request<br><br>/api/class/?action=get_all_classes

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "array of all classes"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Assign Teacher to Class
[Back to the top](#class)
### PUT 
### Expected Request<br><br>
```json
{
    "body": {
        "class_id": 3,
        "teacher_id": 2
    },
    "action": "assign_teacher_to_class" 
}
```
### <br>
| Variable   | Data Type | Required | Additional Validation |
|------------|-----------|----------|-----------------------|
| class_id   | integer   | True     | No                    |
| teacher_id | integer   | True     | No                    |   

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "teacher has been assigned to that class"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```