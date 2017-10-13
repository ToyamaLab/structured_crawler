import tweepy


def getApiInstance():
    consumer_key, consumer_secret = "xxxxx", "xxxxx"
    access_token_key, access_token = "xxxxx", "xxxxx"

    auth = tweepy.API(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    # 利用制限にひっかかた時に必要時間待機する
    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api


# Idで指定されたユーザの全フォロワーを取得する
# Id ... ユーザidでもスクリーンネームでもok
def getFollowers_ids(Api, Id):
    # Cursorを使ってフォロワーのidを逐次的に取得
    followers_ids = tweepy.Cursor(Api.followers_ids, id=Id, cursor=-1).items()

    followers_ids_list = []
    try:
        for followers_id in followers_ids:
            followers_ids_list.append(followers_id)
    except tweepy.error.TweepError as e:
        print(e.reason)

    return followers_ids_list


if __name__ == "__main__":
    screen_name = "lottiso1"  # ロッチの中岡さんのアカウントをスクリーンネームで指定する

    api = getApiInstance()
    f_list = getFollowers_ids(Api=api, Id=screen_name)

    print(len(f_list))  # 数で確認してみる
