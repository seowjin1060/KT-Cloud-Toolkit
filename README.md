# ktcloud_sdk
### 주요 변경 사항
* 사용자 계정 입력 방법
 - SDK 를 실행하면 [ktcloud] api_key : 라는 입력창이 생성되며 사용자 계정 입력함 (secret key도 동일한 방법으로 입력)
* 매번 입력하기 번거로울 때 아래 명령어로 입력해두면 환경변수로 생성됨 (창 열려있는 동안에만..)
 - linux
   + export KTCAPI={APIkey입력}
   + export KTCSEC={SECkey입력}
 - Windows
   + set KTCAPI={APIkey입력}
   + set KTCSEC={SECkey입력}


### install
```
sudo apt install python3-dev
pip3 install pandas
pip3 install requests
```
