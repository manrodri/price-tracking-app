class Item:
    def __init__(self, url, tag_name, query, cookies={}):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self.cookies = cookies

    def load_price(self):
        # business login to load price and return it as a float
        # request, beautifulsoup, strip, regex,...
        pass


'''

john_lewis_url = "https://www.johnlewis.com/apple-watch-series-7-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-regular/p5788434"
another_url = "https://socialblade.com/youtube/user/pewdiepie/realtime"
soccer_stats_url = 'https://www.soccerstats.com/matches.asp?matchday=2&daym=tomorrow'
ebay_url = "https://www.ebay.co.uk/itm/185032451286?epid=3041134620&_trkparms=ispr%3D1&hash=item2b14cb24d6:g:01sAAOSwF9FhM253&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsS7UXID%252BRPOSNsnm8kYPghtD3Gb4V8jGdYP047P6Dr%252Bj9kRutrnwhjICepW1KhGfFfuE%252FKyPMFzGUy0ha9nCsoF3%252BAAxopa8P0F%252Bd8LvrJcbwBPUeIu1r0iQvYEYD%252BWBIRTXXX7NteiJrdE%252F0uJyPmlDZIKb0n4lYObeDF45X2fdB3PzYe71Dg73IBmouzaFq0g4U56Gq9lGTrrzdjkdOatS5HG9GGbJ7nLxq4eyiTmtxQ9CRVkg8dqGvOgC6Cli48vdMClXncJjNXBq26UbwpG%252BWZf40%252FJVV3jR%252B6WhKeQZWaUngEhC%252FrQmqGw1zwK9UCPUvNq6xBUlSxFn2bcgIF3CdHrg1wVesib5%252F8bIGKjEs5EfvvQ3wo2K2rfVqflA2b%252Bw6XHfNwDLsgD%252FbDtA%252BHTfMTWb3FS6PMAjym%252BR8l65GrCPogztGeZ4XDuq8aVuearnx0XDr1rlXho90VYCLF%252FJMYOvTfm%252FWOkNBCtOrjYZOuS9uhqLSHa57I%252FfwHDptrZ3IN7yGDhu5p%252B1ae59vvqV8sFYFcYwdAm%252FBxcV0Iqeq5ZBn6C%252Fby4OptbFkIUCzPTmOcvInTB5cyWX%252F5d39A6%252BltIX1mwvwrlq%252BRjvKBWUN65kwo8tnsX4iXaYUvUeZTyalpajmXrHfyQOovT%252B7hZTTqo52XaUnFLkpm3KBlTemzyV%252B%252BLYnm6aLi50GO4TM3zmgxZDYsPRMdeFNa093vR8ETh2JJoOOwfFzCX7BgosDXaWx5vsGFt9X%252FYa9w%252BGLvVV5Z1N5PvFPXSGnEpilvBbk0ed2yWe38483GqhoC8s2CCS8XVDxAP1NWj2id9dzn%7Cclp%3A2334524%7Ctkp%3ABFBM_pnot8xf"
tesla_url_yahoo_finance = 'https://uk.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'
amazon_url = 'https://www.amazon.co.uk/Titan-Playbook-Iconic-Legendary-History-ebook/dp/B07NRPJNXV/ref=sr_1_1?crid=1KCZARB7A2AIU&keywords=robin+sharma&qid=1642348600&sprefix=robin+sharma%2Caps%2C58&sr=8-1'
argos_url = 'https://www.argos.co.uk/product/9513567'
decathlon_url = 'https://www.decathlon.co.uk/p/speed-skipping-rope-pro/_/R-p-311896'

amz_cookies = {
    "csm-hit": "tb:VWQBBSX0NWR28E70XEYD+s-VWQBBSX0NWR28E70XEYD|1642349540273&t:1642349540273&adb:adblk_no",
    "i18n-prefs": "GBP",
    "session-id": "260-6391902-5169011",
    "session-id-time": "2082787201l",
    "session-token": "Mb3QoRkkfktXLjhUfztywMz2lJ2jIH2GC9Xc0klDmU4hLrQtyyhXgJsgsBxUqi4B0edqB5HmG+ik1TfTOPDTeBkx4q1KaPUgDxXNCq/mzfYHd3XbxiKqOPgif+uzBNodO7aRse4jrDkf8hrcfcnwhvkhuyHmfRHJwmisYeLhNOzc1swAmL+WXSTR1vrv4v3s",
    "ubid-acbuk": "262-5488208-1887655",
}


john_lewis_cookies = json.loads('{"mt.v":"5.473676850.1642350931259","ABSHPB":"1","bm_sz":"981981985E3E37FF3713DB736BF9CF30~YAAQLMF6XBgtPqR9AQAA9m++Yw7Pp6jvhzTzn4rIoIzSmiuhFxQuI6OlONwgneMmTsFzbsUlh+JyO0wLXk69ir65QZBJygVT5H+YX+jG379jjWOtYq+zHrk/MYxAfKzDNo6bEQ7DgoNGPUInIWKCrVl/MDRA00C8kV9c6rZpOAflfOj+hpKPzpYpHvtYy1BkToNs7HHjauJZUg/mSZQeRowt0+Vdlj1z3UrqkYr+U3JwB7pcwhya2PplVw7fLSyvrm2rck8T9bPIPpRKnkvBnGfDYnimmNzKJAgJ4lGjy35qC9IhcZU=~3422003~3553072","ens_session":"1","_scid":"f92c9cd1-fe46-462d-9caf-b2030f18c5c2","rr_rcs":"eF5jYilN9jAwNjJNMUg11E0xMzTRNTFNSdFNNUxL1k0xNU2ztEhNNTNNMwIA1vkK0A","_abck":"9D6E60782029804C6ECC0B076A3261DE~0~YAAQLMF6XGwvPqR9AQAAZ4S+Ywd0v2vFvHof3x+kLAaSyxo6JjTnyrEvP8/k7g4ujzttPJ5xCIWj7ct+4d9EUw3lIJQhG2J36DvF2rWMgUDH0xuQUtAXnFZkB1c9QdL//a0vc6YBqA9NkOXGSApTfDKw3cyo7zycCXVZrlaKGbG+fs5ZDg3Bn6sbjBycYIRdwDTbGpnEgEbqUdWglN5ef15Bn53aLCzTmMk0b++zp/l6gsBpKVAuwxW1sWvY+1PEk8ywZRNkh+6OT+xlZEYpib9h4XQUqpU+cS/Fs8zos1nxCg5m1NT6fdM8ElZtru3LchY+ufk+CUYTXZZR5Yk3G9zzaHybXWbIHC2HZobge2v74HMNkAmdLjs/YwEZtzE2HL2RXpVnu+yUkO9whWFQve/4DQ6gRVJKf7a6~-1~||-1||~-1","JOHNLEWIS_ENSIGHTEN_PRIVACY_BANNER_VIEWED":"1","JOHNLEWIS_ENSIGHTEN_PRIVACY_Advertising":"1","JOHNLEWIS_ENSIGHTEN_PRIVACY_Analytics":"1","JOHNLEWIS_ENSIGHTEN_PRIVACY_Essentials":"1","JOHNLEWIS_ENSIGHTEN_PRIVACY_Functional":"1","JOHNLEWIS_ENSIGHTEN_PRIVACY_Personalisation":"1","s_dfa":"johnlewisonejlprod","ensSearchEventData":"{\\"lastViewedProduct\\":\\"https://www.johnlewis.com/apple-watch-series-7-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-regular/p5788434\\"}","ensRRCookie":"","ensReferringPageType4":"[\\"standard product\\",\\"/apple-watch-series-7-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-regular/p5788434\\",\\"no previous page type\\"]","_uetsid":"690bb07076ea11ec95c599af658a88c3","_uetvid":"690c0d5076ea11ec9c8c034d2fbac326","_cls_v":"b8a60849-6163-44fb-b780-d70a067c43d6","_cls_s":"e411c137-1931-4fe1-adea-ff35b85eb8f3:0","_qubitTracker":"oz9tmqpgo8w-0kyhhd2vp-0l4wb74","ensFindingMethod":"{\\"method\\":\\"other\\",\\"productId\\":\\"5788434\\"}","qb_generic":":X5jvwTT:johnlewis.com","_gcl_au":"1.1.422452410.1642350970","_ga_S1ZHFBNH86":"GS1.1.1642350969.1.0.1642350970.0","_fbp":"fb.1.1642350970170.1878415861","s_fid":"3B07AA73E89939C2-2C911153BE9300DE","gpv_pn":"jl:electricals:smart watches & wearable tech:view all smart watches:5788434","s_ppvl":"[[B]]","s_cc":"true","ensCustomFindingMethod":"","s_vi":"[CS]v1|30F224BD04710F8E-400007F6C88AB752[CE]","eds":"INS-623499590:762563817-1642350969","_pin_unauth":"dWlkPU1ERTRZMlEzWmpNdFlUYzJOaTAwT0RRMExXRmpOR0V0TnpJME0ySmtOekJrTVdNMg","_ga":"GA1.2.1978407500.1642350970","_gid":"GA1.2.25126008.1642350970","qb_permanent":"oz9tmqpgo8w-0kyhhd2vp-0l4wb74:1:1:1:1:0::0:1:0:Bh5El6:Bh5El6:::::92.0.181.118:haringey:32407:united kingdom:GB:51.58:-0.12:itv london:826044:haringey:25430::::X5jvwYQ:X5jvwYN:0:0:0::0:0:johnlewis.com:0","_gat_gtag_UA_34398547_21":"1","qb_session":"1:1:4::0:X5jvwYN:0:0:0:0:johnlewis.com","s_ppv":"jl%3Aelectricals%3Asmart%20watches%20%26%20wearable%20tech%3Aview%20all%20smart%20watches%3A5788434,17,17,969,1431,969,2560,1080,1,L","ecos.dt":"1642351004394"}')


argos_json_string = '{"analytics_channel":"ecomm","mdr_browser":"Akamai","akaas_arg_uk_randval":"85","PDP_Test_Group_1":"2","bm_sz":"802BD96D8EC438F2A13191936FB0EB75~YAAQRg8DF6bRkGN+AQAAiU60Yw7BgjKl+D/7x+DDZg1JIcXsojZHHOlH9ykKYzx48cB0x0XpCtsmKGlqXxpMAnOitG5wjkYaGwznElzB9jEaTWx0gkKAWzHFjGkxITrZj3W8uKdnZxBJfu297LnYVhVbIYoD7ogoIOz/aOA4YMYXJafwcmErMmvQK/3wSj7DNaaJPCAPbL7S3NLJkmXiEaHQ8cakxfA9DJj+WRXDie1330wPvkNJhzdYqdVm6vGLZN9//mLV5cXGfXtlv7nkV4pJpyzZ1Z5OiKC8PbtmNdeSi4HX~3356213~3486513","newConsentServed":"true","cisId":"09eac24e2fb04f68bafe5127da702857","Checkout_Test_Group_1":"3","akaas_arg_uk_global":"1650126268~rv=85~id=eb3a0230bfd2671cfa26b18ec7475a85","RT":"\\"z=1&dm=www.argos.co.uk&si=c2d3b3a2-baee-42d3-b602-d2a22cd8a3c2&ss=kyhgy14l&sl=1&tt=jd&rl=1&ld=ok\\"","AMCVS_095C467352782EB30A490D45%40AdobeOrg":"1","AMCV_095C467352782EB30A490D45%40AdobeOrg":"1406116232|MCMID|33364451086748927264088148673262898887|MCAAMLH-1642955068|6|MCAAMB-1642955068|6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y|MCOPTOUT-1642357468s|NONE|MCSYNCSOP|411-19016|vVersion|2.5.0","_abck":"6A638C9667ED2B7666C1589A1D384404~0~YAAQRg8DF+3RkGN+AQAA/1K0YwcUo3DyMV2cC6h97WLVU16DQJAJKJQmmvzvi7uFdL+5WtT2yxdfxCOZncAd4I8i8pcpMQIYnxWEni95nGqBdLU4kNcxE4+E2Nph08TUJltVsmnEw7oCeBx/C8pkz0buPIlkOFtcPwsM1aPsDz7lccJtJ0UFDnHkb5XYT9u7DLSbLyFQzKU7JgeyWt4q8Wg81oLtwBDMGGC3qNJMBVEHjQ5gtKAndQ6sNaYfAwTTA1aGSm/E9WVjbMow85Kuu+VU482B9LJoxM7Q9d4uv4j9Z8oFFHf4gfT1Ww6cDhHXQXsfzpodOpwXMmnVdaQUS+Vsw7Q4CjpWBCU1noy8tWIgetwqzZwdvLWYSainzxCrv30CV3nlHfBfCkf313LkjPLaPwK0S4pOng==~-1~||-1||~-1","prev_vals":"ar:pdp:9513567:applewatchseries7gps41mmgreenalucase/sportband:*|*ar:productdetails:","CONSENTMGR":"consent:true|ts:1642350343650","_gcl_au":"1.1.677950254.1642350344","_fbp":"fb.2.1642350343984.1756590409","_scid":"949b95ea-ecdc-40da-82f9-d133ac16a1b9","stimgs":"{\\"sessionId\\":88867101,\\"didReportCameraImpression\\":false,\\"newUser\\":true}","syte_uuid":"f40f0cc0-76e8-11ec-9178-cd6a12e05dbc","_uetsid":"f4128cb076e811ec934c5d364280742e","_uetvid":"f412c91076e811ec88a1b52c7c316a1c","BVBRANDID":"f1dd62cf-70e7-4e0a-86db-428ab2040503","BVBRANDSID":"4a1ebede-5cab-42f6-809a-c1fa45a37fe0","CRTOABE":"0","_pin_unauth":"dWlkPVpHWXdPV00xTlRZdE56RTJOUzAwTUdFNUxUazVNV010T0dVNU9ERXdOamMzWm1RMg","sc.ASP.NET_SESSIONID":"1o5rqpsi22uzm25i0hvvpjam","_ga":"GA1.3.1766635850.1642350344","_gid":"GA1.3.357331767.1642350344","_gat_gtag_UA_50023582_1":"1","_taggstar_ses":"f4608ade-76e8-11ec-a2dc-590aa29c55e5","_taggstar_vid":"f4608ade-76e8-11ec-a2dc-590aa29c55e5","_taggstar_exp":"v:3|id:tvt2|group:control","_4c_":"fVJtb5swEP4rlaV9CwS/YpCmaWunah8mVc32GRnjFBQaLOOEdVX++84JkCqJxofj7rl77sV372iozRblWDBCeUKZJJQs0Ma89Sh/R9oGuQ9i51qUo9p72+fL5TAMsXIvXR/rLt5tltZ11U77ZcYx5SL9ottGb1bPn/vW5t6411xZ25pPJBmU1zX8e+Ma04OS5jjPkhyjBdJdZaAGzmIZB9v/BSsBxWyhBWRdBfpYqfBvNgQPprzrqw04KrNvtCmGpvI1OAgXyRmtTfNS+5A8kUfYumCANjTbqhtmGmb0AzrTMpEB+vTwVPwyvS8eXbezBQ5lAF4Z5XR96bnpICfHN9cNvXn+vrpBuukbefe10Ztu5y9pFHzlkRfGuq9d92rushTQDvaIfioNqjNr49wxAqy+8eH9PixxBGH3Ex6eez++U9tp1QYGnMsCPX4tfv94CK5UCEG55Ek83xBDhwX6czoqRkXKBBUc1unhgqRgSfggwjXVeF0oVXItqopFLNMyYkLxqCRiHVGcEVmuVZYk4aGPOXmCiYAiICDJvplylJhJKksaMSUwJCJVBF2VkZGMq1JJKYlBc1+UE8wgiRz7wnJqy7ZjRnwOFixljPJsCmbzEHZ/FX0cGQS+Hvm0o/9wyDVnXZbTiD26IJz7nwmHwz8=","utag_main":"v_id:017e63b4504a00125157c973464705078005a07000e50$_sn:1$_se:5$_ss:0$_st:1642352148561$ses_id:1642350268491;exp-session$_pn:1;exp-session$dc_visit:1$dc_event:3;exp-session$dc_region:eu-west-1;exp-session"}'
argos_cookies = json.loads(argos_json_string)
decathlon_cookies = json.loads('{"didomiVendorsConsent":"iab:11,iab:24,didomi:twitter,didomi:google,c:salecycle,c:pixelimg-87TtKAVP,c:ysance-3xwFx9e7,c:youtube,c:clicktale,c:rakutenad-wQdcrqNm,c:shop2mark-Yz3dm3eD,c:mopubad-aPkpRVbP,c:abtastyg-XEjCJgEL,c:mopiniong-XKtap2Up,c:trustpilo-aZthbTzP,c:constructo-Dk273Vq6,c:luckycycl-PFFiHweR,c:reservein-4PwzZqMH,c:cashbacki-HgbnbEzK,c:crypto-kkYKzP8x,c:googlerem-RXHhiXrR,c:heydaych-gErm4EWT,c:insiderta-Et9Kh6q6,c:analytics-UiBArJJK,c:microsoft,c:cookiesan-aY7WekKr,c:precisetv-PL7XgJRx,c:facebookg-6kGcXhr3,c:contentsq-VxQcMzpH,c:dynamicyi-ETeaxHck,","PLAY_LANG":"en","nlbi_989924":"LUI6V6o1bnfoQmJQKaszZwAAAAB6aMSNBqKAnhFv5hG8Yb5R","incap_ses_47_989924":"uAGJPXiuyGvSEcOTUPqmAIpK5GEAAAAAcb/vvxEpvXKFX1WARvqbfg==","incap_ses_1371_989924":"HRWdYrqC6SETT6SemcUGE4pK5GEAAAAAGdt0YgwIlrwlqslaBVa9Ug==","incap_ses_873_989924":"N816S0HHrTrz6PQcL4UdDIpK5GEAAAAAgWUGSCk37xbz6Ao9YaLsJw==","ABTasty":"uid=cbeny30mjpfasr4r&fst=1642351243319&pst=-1&cst=1642351243319&ns=1&pvt=1&pvis=1&th=","ku1-sid":"0p7omsKtpUlXDv_fHJxDB","ku1-vid":"7283a4c5-f35c-dc9e-e7d7-b637e91ee8d4","incap_ses_1183_989924":"0eYGKY3TxCQnjPzZxNxqEItK5GEAAAAAFxC4TUDknUxrAfWdcutO4g==","ABTastySession":"mrasn=&sen=0&lp=https%3A%2F%2Fwww.decathlon.co.uk%2Fp%2Fspeed-skipping-rope-pro%2F_%2FR-p-311896","incap_ses_869_989924":"U3/9MFxUf0rje/Nnc08PDItK5GEAAAAAe9CWj9D0N1bennGeqDDA7w==","tc_cj_v2":"^cl_]ny[]]_mmZZZZZZKPNLMOKLNNJPOZZZ]","nlbi_989924_2498875":"zdAkJLa5gzb1lfyQKaszZwAAAAA5CVrr2jIzQ6qpjxzZb2mU","rxVisitor":"1642351244194U5NO16R90A97LN6527OEO9U7OJ5UDBCB","dtLatC":"1","dtSa":"-","_ga":"GA1.3.DKT-65e0dad6-672c-4dfd-b1f4-a13c724c41a5","_gid":"GA1.3.1998872285.1642351244","_gat_transcript":"1","dtCookie":"v_4_srv_2_sn_424B198D4C9C55190F4ED801830CE5FD_app-3A3dc3c78d953a04b6_0_ol_0_perc_100000_mul_1","didomi_token":"eyJ1c2VyX2lkIjoiMTdlNjNjMzMtMzM5OC02ZjBlLWEyNzEtMzVjZGQ3NjFiMWExIiwiY3JlYXRlZCI6IjIwMjItMDEtMTZUMTY6NDE6MDcuODkwWiIsInVwZGF0ZWQiOiIyMDIyLTAxLTE2VDE2OjQxOjA3Ljg5MFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsidHdpdHRlciIsImdvb2dsZSIsImM6c2FsZWN5Y2xlIiwiYzpwaXhlbGltZy04N1R0S0FWUCIsImM6eXNhbmNlLTN4d0Z4OWU3IiwiYzp5b3V0dWJlIiwiYzpjbGlja3RhbGUiLCJjOnJha3V0ZW5hZC13UWRjcnFObSIsImM6c2hvcDJtYXJrLVl6M2RtM2VEIiwiYzphYnRhc3R5Zy1YRWpDSmdFTCIsImM6bW9waW5pb25nLVhLdGFwMlVwIiwiYzp0cnVzdHBpbG8tYVp0aGJUelAiLCJjOmNvbnN0cnVjdG8tRGsyNzNWcTYiLCJjOmx1Y2t5Y3ljbC1QRkZpSHdlUiIsImM6cmVzZXJ2ZWluLTRQd3pacU1IIiwiYzpjYXNoYmFja2ktSGdibmJFeksiLCJjOmNyeXB0by1ra1lLelA4eCIsImM6Z29vZ2xlcmVtLVJYSGhpWHJSIiwiYzpoZXlkYXljaC1nRXJtNEVXVCIsImM6aW5zaWRlcnRhLUV0OUtoNnE2IiwiYzphbmFseXRpY3MtVWlCQXJKSksiLCJjOmNvb2tpZXNhbi1hWTdXZWtLciIsImM6cHJlY2lzZXR2LVBMN1hnSlJ4IiwiYzpmYWNlYm9va2ctNmtHY1hocjMiLCJjOmNvbnRlbnRzcS1WeFFjTXpwSCIsImM6ZHluYW1pY3lpLUVUZWF4SGNrIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbIm1hcmtldGluZy1NUlpWcHJlYSIsImFuYWx5dGljcy1HTWdCV0dUaCIsInBlcnNvbmFsaXMtdGY4cFpUVkgiXX0sInZlbmRvcnNfbGkiOnsiZW5hYmxlZCI6WyJnb29nbGUiLCJjOm1vcGluaW9uZy1YS3RhcDJVcCJdfSwicHVycG9zZXNfbGkiOnsiZW5hYmxlZCI6WyJhbmFseXRpY3MtR01nQldHVGgiXX0sInZlcnNpb24iOjIsImFjIjoiQkFlQUVBVVlDQTRBLkJBZUFFQVVZQ0E0QSJ9","euconsent-v2":"CPS6upnPS6upnAHABBENB9CgAP_AAE_AAAwIF5wAwAFgAYAXmBecAIABYC8wAAAA.f_gACfgAAAAA","didomi_cookies":"essential,analytics,marketing,social","_dyid":"6187946881786858123","_dyjsession":"pj2r37nggo4aw0egy8ba6azjuhumj9yi","_dy_csc_ses":"pj2r37nggo4aw0egy8ba6azjuhumj9yi","_dy_soct":"1058840.1150461.1642351243","dy_fs_page":"www.decathlon.co.uk/p/speed-skipping-rope-pro/_/r-p-311896","_dy_toffset":"0","_dyfs":"1642351243619","_dy_df_geo":"United Kingdom..Bethnal Green","_dy_geo":"GB.EU.GB_ENG.GB_ENG_Bethnal Green","_dycnst":"dg","_dycst":"dk.m.c.ws.","_cs_mk_ga":"0.2172020952699396_1642351267943","__ywtfpcvuid":"4135902611642351268027","__ywtfpcsuid":"20090685921642351268029","_gcl_au":"1.1.950532076.1642351268","rxvt":"1642353068167|1642351244196","_fbp":"fb.2.1642351268251.1611015706","Pastease.passive.chance.Cmjx4TLOsJoZSQn":"chance40.2","Pastease.passive.activated.Cmjx4TLOsJoZSQn":"0","_uetsid":"1af381a076eb11ecbe5829718120306b","_uetvid":"1af48a6076eb11ec9e4eb5826d3421b9","dtm_token_sc":"AQEHoc1wiNVjCwFTrsCnAQEBAQA","_cs_c":"1","_cs_id":"cb6081ed-e806-a978-e109-101eeae428e9.1642351268.1.1642351268.1642351268.1.1676515268449","_cs_s":"1.0.0.1642353068453","dtPC":"2$151244191_599h-vKVFROLPKEWUUNSVGJMALHHHMLTMKRKEC-0e0","dtm_token":"AQEHoc1wiNVjCwFTrsCnAQEBAQA","dtm_tcdata":"CPS6upnPS6upnAHABBENB9CgAP_AAE_AAAwIF5wAwAFgAYAXmBecAIABYC8wAAAA.f_gACfgAAAAA","stc120919":"tsa:1642351268680.435839404.9735718.18090921480497935.:20220116171108|env:1|20220216164108|20220116171108|1|1104306:20230116164108|uid:1642351268679.1909372262.9442058.120919.1487851543:20230116164108|srchist:1104306:1:20220216164108:20230116164108"}')


# print(type(argos_cookies))

TAG_NAME = "div"
QUERY = {"class": "prc__active-price"}

response = requests.get(decathlon_url)
content = response.content

print (content)
# data = response.text
#
#
soup = BeautifulSoup(content, 'html.parser')

# print(soup.find_all(TAG_NAME))

# all_matches = re.findall(r"""<a class='button' style='background-color:#AAAAAA;font-color=white;' href='(.*?)'>""", data)


element = soup.find(TAG_NAME, QUERY)
#
# string_price = element.text.strip()strip

# print(f"string_price: {string_price}")
print(f'element: {element}')
# print(f"all_matches: {all_matches}")


#
# item = Item(url, tag_name, query)
# item.load_price()

'''
