import requests

def getFacebookPosts():
    response = requests.get(
        url='https://www.facebook.com/',
        headers={
            'Cookie': 'sb=7vzLXfXUcWBh2sSxUb2G7_Bh; datr=7vzLXWIGQLIr69fb0F8DBsHN; dpr=1.2000000476837158; c_user=100000195922642; xs=44%3AZ8fz3tViqmszaQ%3A2%3A1573649661%3A7745%3A11317; spin=r.1001513817_b.trunk_t.1575902878_s.1_v.2_; fr=1y1lDy11LZ61ldgWC.AWUQ4uPG4Ib4mYZ4po4pin4Fb-U.Bdy_zu.U3.F3l.0.0.Bd7mwj.AWUplo6A; wd=150x600; presence=EDvF3EtimeF1575906424EuserFA21B00195922642A2EstateFDutF1575906424862CEchFDp_5f1B00195922642F1CC'
        }
    )
    if response.status_code != 200:
        print(f'status is not 200({response.status_code})')
        return
    with open('facebook.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    getFacebookPosts()