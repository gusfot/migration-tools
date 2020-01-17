Migration Tools
- 설명: 각종 데이터 포맷을 원하는 데이터 포맷으로 변경한다.
- Speck: 
    - python3.x
    - mysql5.5이상

1. excel(csv) to mysql(mariadb) migration
    - 사용법: python migration mig -f [파일경로]
        - 엑셀파일의 시트명은 테이블명으로 맵핑한다.
        - 엑셀파일의 첫번째ROW는 컬럼명으로 한다.
        - 엑셀파일의 두번째ROW부터는 데이터로 한다. 
        - csv파일의 경우, -n (테이블명) 옵션을 설정한다.
        - conf/config.py에 db 정보를 세팅한다.
        - db 계정권한에서는 CREATE, SELECT, INSERT 권한이 필요한다. (create table, insert, truncate 등)
    - 도움말: python migration mig --help
      - 옵션
          - -f TEXT  (파일전체경로)  [필수]       : 엑셀 파일경로(파일명포함)
          - -t       (테이블비우기)                   : 기존 테이블의 데이터를 비우고, 새로 입력한다.
          - -c       (테이블생성하기)                 : 기존테이블이 없는 경우, 테이블을 생성하여 데이터를 입력한다. (단, 같은 이름의 테이블이 있는경우, Prefix(YYYYMMDDHHmmss_) 를 테이블명에  추가한다.)
          
