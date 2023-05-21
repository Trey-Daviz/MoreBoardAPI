[Back to main](../README.md)
# Generic
[Login](#login)<br>
<br><br>

# Endpoint: /Login

## Login
[Back to the top](#generic)
### GET /api/generic/login
### Expected Request <br><br>/api/generic/login?username=TD600001&password=password1<br>

| Variable | Data Type | Required | Additional Validation |
|----------|-----------|----------|-----------------------|
| username | string    | True     | No                    |
| password | string    | True     | No                    |   

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "True|False"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```