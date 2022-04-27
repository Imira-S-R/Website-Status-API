## Website-Status-API
An API to find the status of any website.

## How to use
This API is FREE & does not require an api-key. Simply run the following.
```js

https://1714jv.deta.dev/check-status?url=URL

```
## Correct response
### Request
```js

https://1714jv.deta.dev/check-status?url=https://www.google.com

```
### Response
```js

{"url": "https://www.google.com", "status-code": 200, "response-time": 313.6}

```
## NOTE
#### Use the correct protocol: ex-> http://, https://
#### Do not include inverted comma for the url.
