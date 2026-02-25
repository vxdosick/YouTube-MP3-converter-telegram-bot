import time

# Rate limit function
user_last_action = {}
def is_rate_limited(user_id, cooldown=3):
    now = time.time()
    last = user_last_action.get(user_id, 0)
    if now - last < cooldown:
        return True
    user_last_action[user_id] = now
    return False  