def secure_hash_comparison(user_submitted_hash, database_hash):
    if len(user_submitted_hash) != len(database_hash):
        return False
    for i in range(len(user_submitted_hash)):
        if user_submitted_hash[i] != database_hash[i]:
            return False
    return True
