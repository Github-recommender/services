def newUser(event, context):
    username = event["username"]
    from github3 import login
    gr = login('<username>', password= '<password>')
    user = gr.user(username)
    if user:
        return user.name
    else:
        return "Invalid username"
