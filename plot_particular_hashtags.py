#Write code to determine number of images shared with a particular hash tag and plot the same using matplotlib.

import requests
import matplotlib.pyplot as plt

APP_ACCESS_TOKEN = '5629236876.1cc9688.86db895c038043b5960dc2949785299a'
BASE_URL = 'https://api.instagram.com/v1/'

def plot_particular_hashtags(list_of_hashtags):
    number = []
    for tags in list_of_hashtags:
        try:
            request_url = (BASE_URL + 'tags/%s?access_token=%s') % (tags,APP_ACCESS_TOKEN)
            tags_info = requests.get(request_url).json()
            if tags_info['meta']['code'] == 200:
                if len(tags_info['data']):
                    number.append(int(tags_info['data']['media_count']))
        except:
            number.append(int(0))
    #plotting pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(number, labels=list_of_hashtags, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

#example call
if __name__ == "__main__":
    plot_particular_hashtags(['dominos','mcdonalds','subway','pizzahut'])