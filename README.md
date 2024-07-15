<h1 align="center">
  <a href="https://reactnative.dev/">
    React Native
  </a>
</h1>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all package needed.

```bash
pip install -r requirements.txt
```
## Running App

**Running Recomended**
```bash
python3 manage.py runserver 0.0.0.0:8000
```



## Register

```http
POST /api/v1/register 
```
| Body (JSON) | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `username`| `string` | **Required**.|
| `password`| `string` | **Required**.|
| `Email`| `string` | **Required**|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `X-Gue`| `token` | **Required**.|


## Login

```http
POST /api/v1/login 
```
| Body (JSON) | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `username`| `string` | **Required**.|
| `password`| `string` | **Required**.|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `X-Gue`| `token` | **Required**.|


## Logout Users

```http
GET /api/v1/logout
```

| Body (JSON) | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `id_users`| `integer` | **Required**.|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|


## Profile Users

```http
GET /api/v1/profile/<str:username> 
```

| Params | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `username`| `string` | **Required**.|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|


## Update Profile Users

```http
POST /api/v1/profile/update/<int:id> 
```

| Params | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `id`| `integer` | **Choice**.|

| Body (Form-Data) | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `username`| `string` | **Required**.|
| `profile`| `file [PNG,JPEG]` | **Choice**.|
| `name`| `string` | **Choice**.|
| `bio`| `string` | **Choice**.|



| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|


## Follow & Unfollow Users

*For `Follow` and `Unfollow`, there is in the same request, if you want to unfollow, do it  request  as `Follow`, send the same request*

```http
GET /api/v1/follow/<int:id> 
```

| Params | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `id`| `integer` | **Required** , *Your Id*|

| Body (JSON) | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `id_users`| `integer` | **Required** , *Id Your Want Follow*|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|


## Posting Tweet & Reply Tweet

```http
POST /api/users/v1/posting
```

| Body (Form-Data) | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `users`| `integer` | **Required** , *Your Id Users*|
| `content`| `string` | **Required**.|
| `media`| `file, [JPEG.PNG,JPG,GIF]` | **Choice**.|
| `typeretwet`| `boolean` | **Choice**, Default False, *If You Want Retwet this Fields Required and Change to true*|
|`wheretweet`|`integer`|**Choice**, *Required If Reply (typeretwet) true , Id From Feeds You Reply*|



| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|


## Request All Tweet (Not Reply Tweet)

```http
GET /api/users/v1/tweet
```

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|

## Request Reply Tweet Based On Id Tweet

```http
GET /api/users/v1/retweet/<int:id>
```
| Params | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `id`| `integer` | **Required** , Id Feeds|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|

## Request Reply Tweet All 

```http
GET /api/users/v1/retweet
```

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|

## Request Single Tweet

```http
GET /api/users/v1/tweet/<slug:slug>
```
| Params | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `slug`| `uuid4` | **Required** , uuid Feeds|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|

## Like & Unlike Tweet

*For `Like` and `Unlike`, there is in the same request, if you want to unlike, do it  request  as `Like`, send the same request*

```http
GET /api/users/v1/likes/<int:id>/<int:author>
```
| Params | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `id`| `integer` | **Required** , id Feeds|
|`author`|`integer`|**Required**, id users|

| Authorization | Type    | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer`| `token` | **Required**.|
