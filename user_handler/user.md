[Back to main](../README.md)
# User
[Add User](#add-user)<br>
[Remove User](#remove-user)<br>
[Get All Classes From Teachers](#get-all-classes-from-user)<br>
[Get All Users](#get-all-users)<br>
[Get User Info](#get-user-info)<br>

# Endpoint: /User

## Add User
[Back to the top](#user)
### POST 
### Expected Request<br><br>
```json
{
    "body": {
        "firstname": "Trey",
        "lastname": "Davis",
        "user_password": "password3",
        "email": "something@something.com",
        "role_id": 0,
        "grade": 11
    },
    "action": "add_user"
}
```
### <br>

| Variable      | Data Type | Required | Additional Validation                                              |
|---------------|-----------|----------|--------------------------------------------------------------------|
| firstname     | string    | True     | No                                                                 |
| lastname      | string    | True     | No                                                                 | 
| user_password | string    | True     | Minimum 8 characters.  At least one letter and at least one number |
| email         | string    | True     | Looks for something like something@something.something             |
| role          | integer   | True     | Looking for a valid role_id.  Currently that's something from 0-3  |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User added"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Remove User
[Back to the top](#user)
### DELETE /api/user/remove_user
### Expected Request ?user_id=559&action=remove_user<br><br>
### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| user_id  | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "User Removed"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get All Classes From User
[Back to the top](#user)
### GET
### Expected Request ?user_id=6&action=get_all_classes_of_user<br><br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| user_id  | integer   | True     | No                                                                 |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "a list of all the class data for the user"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```

## Get All Users
[Back to the top](#user)
### GET 
### Expected Request: ?role_id=-1&action=get_all_users<br><br>

### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| role_id  | integer   | True     | No                                                                 |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "a list of all of the users if role id = -1, filtered by role if role_id is a valid role"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```


## Get User Info
[Back to the top](#user)
### GET
### Expected Request: ?user_id=6&action=get_user_info<br><br>

### <br>

| Variable | Data Type | Required | Additional Validation                                              |
|----------|-----------|----------|--------------------------------------------------------------------|
| user_id  | integer   | False    | No                                                                 |


### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "All user info from one user"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```
