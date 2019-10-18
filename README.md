# checkingFace

Add authentication with JWT in rails API, endpoints

https://api-jwt-v3.herokuapp.com/api/users POST allows creating a new user .  
https://api-jwt-v3.herokuapp.com/api/users/login POST, to log in a user with password and email, and returns a JWT token to retrieve the user info in JSON

https://api-jwt-v3.herokuapp.com/api/user, GET show a user, you must send in Authorization Header a Bearer token

https://api-jwt-v3.herokuapp.com/api/user, PATCH or PUT, you must send in Authorization Header a Bearer token
https://api-jwt-v3.herokuapp.com/api/all, GET returns all users in database, this is a public endpoint
