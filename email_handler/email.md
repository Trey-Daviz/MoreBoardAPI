[Back to main](../README.md)
# Generic
[Email User](#email-user)<br>
<br><br>

# Endpoint: /Email

## Email User
[Back to the top](#generic)
### POST
### Expected Request<br><br>
```json
{
    "body": {
        "email_to": [2],
        "email_subject": "Test",
        "email_body": "Test email"
    },
    "action": "send_email"
}
```
### <br>

| Variable      | Data Type         | Required | Additional Validation |
|---------------|-------------------|----------|-----------------------|
| email_to      | array of integers | True     | No                    |
| email_subject | string            | True     | No                    |
| email_body    | string            | True     | No                    |

### <br>Expected Response:<br>
#### Healthy Call
```json 
{
    "message": "Email Sent"
}
```
#### Unhealthy Call
```json 
{
    "error": "error message"
}
```