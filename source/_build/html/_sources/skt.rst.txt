RUUT 서비스 가이드
=======================================
RUUT 의 모든 서비스는 REST API 호출 기반으로 이루어져 있습니다. 전체적인 서비스 사용 절차는 아래 그림과 같습니다.

.. image:: ../images/service/usage.png

.. _general_authentication:

인증 (공통 프로세스)
--------------------------
계정 생성
''''''''''''''''''''''''''
API 호출을 통해 로그인을 수행하고 접근 권한을 담은 token 을 부여 받습니다.

.. rst-class:: table-width-fix
.. rst-class:: text-align-justify

============= =====================================
   **POST**   `/api/auth/v1/join`
============= =====================================
 
- Header

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+--------------+--------+------------------+--------------+
| option       | Type   | Default          | Description  |
+==============+========+==================+==============+
| Content-Type | string | application/json | content type |
+--------------+--------+------------------+--------------+

- Body

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

==========  ========  ========================
Key         Type      Description
==========  ========  ========================
username    String    사용자 ID
----------  --------  ------------------------
password    String    패스워드
----------  --------  ------------------------
email       String    사용자 이메일 주소
----------  --------  ------------------------
phone       String    휴대폰 번호 (01x-xxxx-xxxx)
==========  ========  ========================


.. role:: underline
        :class: underline

- Example Code

:underline:`Request`

.. code-block:: none

    content-type:"application/json"

    {
        "username":"example",
        "password":"1234",
        "email":"example@mail.com",
        "phone":"010-0000-0000"
    }

:underline:`Response (code: 200)`

* 별도 응답 body 없음

.. rst-class:: text-align-justify

로그인 (인증 토큰 획득)
''''''''''''''''''''''''''
API 호출을 통해 계정을 생성 합니다.

.. rst-class:: table-width-fix
.. rst-class:: text-align-justify

============= =====================================
   **POST**   `/api/auth/v1/login`
============= =====================================

- Header

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+--------------+--------+------------------+--------------+
| option       | Type   | Default          | Description  |
+==============+========+==================+==============+
| Content-Type | string | application/json | content type |
+--------------+--------+------------------+--------------+

- Body

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

==========  ========  ========================
Key         Type      Description
==========  ========  ========================
username    String    사용자 ID
----------  --------  ------------------------
password    String    패스워드
==========  ========  ========================


.. role:: underline
        :class: underline

- Example Code

:underline:`Request`

.. code-block:: none

    content-type:"application/json"

    {
        "username":"example",
        "password":"1234",
    }

:underline:`Response (code: 200)`

.. code-block:: json

    {
        "token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXNhZG1pbkB0aG…",
        "refreshToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXNhZG1…"
    }

토큰 갱신
''''''''''''''''''''''''''
API 호출을 통해 만료된 인증 토큰을 갱신 합니다.

.. rst-class:: table-width-fix
.. rst-class:: text-align-justify

============= =====================================
   **POST**   `/api/auth/v1/token`
============= =====================================

- Header

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+--------------+--------+------------------+--------------+
| option       | Type   | Default          | Description  |
+==============+========+==================+==============+
| Content-Type | string | application/json | content type |
+--------------+--------+------------------+--------------+

- Body

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

=============  ========  ========================
Key            Type      Description
=============  ========  ========================
refreshToken   String    갱신 토큰 정보
=============  ========  ========================


.. role:: underline
        :class: underline

- Example Code

:underline:`Request`

.. code-block:: none

    content-type:"application/json"

    {
        "refreshToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXNhZG1…"
    }

:underline:`Response (code: 200)`

.. code-block:: json

    {
        "token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXNhZG1pbkB0aG…",
        "refreshToken": "yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJdWIiO…"
    }


패스워드 변경
''''''''''''''''''''''''''
API 호출을 통해 패스워드를 변경 합니다.

.. rst-class:: table-width-fix
.. rst-class:: text-align-justify

============= =====================================
   **POST**   `/api/auth/v1/changePassword`
============= =====================================

- Header

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+--------------+--------+------------------+--------------+
| option       | Type   | Default          | Description  |
+==============+========+==================+==============+
| Content-Type | string | application/json | content type |
+--------------+--------+------------------+--------------+

- Body

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

=============  ========  ========================
Key            Type      Description
=============  ========  ========================
password       String    기존 패스워드
-------------  --------  ------------------------
newPasswrod    String    변경할 패스워드
=============  ========  ========================


.. role:: underline
        :class: underline

- Example Code

:underline:`Request`

.. code-block:: none

    content-type:"application/json"

     {
        "passwrod":"1234",
        "newPassword":"5678",
    }

:underline:`Response (code: 200)`

* 별도 응답 body 없음


패스워드 리셋 (이메일 연동)
''''''''''''''''''''''''''
API 호출을 통해 패스워드를 변경 합니다.

.. rst-class:: table-width-fix
.. rst-class:: text-align-justify

============= =====================================
   **POST**   `/api/auth/v1/resetPasswordByEmail`
============= =====================================

- Header

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+--------------+--------+------------------+--------------+
| option       | Type   | Default          | Description  |
+==============+========+==================+==============+
| Content-Type | string | application/json | content type |
+--------------+--------+------------------+--------------+

- Body

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

=============  ========  ========================
Key            Type      Description
=============  ========  ========================
email          String    회원 정보에 등록된 메일 주소
=============  ========  ========================


.. role:: underline
        :class: underline

- Example Code

:underline:`Request`

.. code-block:: none

    content-type:"application/json"

    {
        "email":"example@mail.com"
    }

:underline:`Response (code: 200)`

.. code-block:: none

    {
        "password": "WEx8Ekp1rT"
    }

RUUT 고유 API 활용
--------------------------

RUUT 고유 API 는 JSON 형태로 실시간 교통 정보, 예측 교통 정보, 돌발(사고 및 이벤트) 정보, V2X 서비스 구독 등의 기능을 제공하고 있습니다. 앞서 인증 과정에서 발급받은 API 접근 키 API 헤더에 포함 시킨 후 
:ref:`API규격 <apidoc>`에 따라 원하는 정보를 요청 하시면 됩니다. 

- Header

.. rst-class:: table-width-fix
.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+---------------------+--------+------------------+--------------+
| option              | Type   | Default          | Description  |
+=====================+========+==================+==============+
| Content-Type        | string | application/json | content type |
+---------------------+--------+------------------+--------------+
| X-Authorization     | string | {accessToken}    | API Key      |
+---------------------+--------+------------------+--------------+

실시간 교통 정보
''''''''''''''''''''''''''

실시간 교통 정보를 획득 하려면 API URL 에 하기 항목을 명시하셔야 합니다. 

* :ref:`Geo filtering <geofilter>` 교통 정보 탐색하고자 하는 지리적 영역 규정 (`filter_type`)
* 획득 하고자 하는 정보의 유형 및 카테고리 선택 (`rttiField`, `lane`)
* 위치 참조 방식 선택 (`lr`)

:underline:`Request Example`

.. code-block:: none

  // 원형 geo filter, 모든 교통 정보 표출, 위치 참조 모두 표출, 차선 단위 정보 배제
  ruut/v1/segments?filter_type=circle&center=37.397619, 127.112465&radius=10&rttiField=all
  &lr=all&lane=off


예측 교통 정보
''''''''''''''''''''''''''

예측 교통 정보를 획득 하려면 API URL 에 하기 항목을 명시하셔야 합니다. 

:underline:`예) 09:00 부터 1시간 동안의 예측 데이터를 20분 단위로 요청 (09:00, 09:20, 09:40 분 예측 데이터 반환)`

* 실시간 교통 정보 획득 정보 포함
* 예측 시작 시점 (`start_time`: 20200101090000)
* 얼마나 오래 데이터를 추출 해야 하는지 (`duration`: 60)
* 몇 분 간격으로 데이터를 추출 해야 하는지 (`interval`: 20)

:underline:`Request Example`

.. code-block:: none

  ruut/v1/segments?filter_type=circle&center=37.397619, 127.112465&radius=10&rttiField=all
  &regionId=0&lr=all&start_time=20200101090000&duration=60&interval=20


돌발 정보 (이벤트, 사고)
''''''''''''''''''''''''''

돌발 정보를 획득 하려면 API URL 에 하기 항목을 명시하셔야 합니다. 

:underline:`예) 모든 돌발 정보를 1번 도로 레벨에 한하여 모든 위치 참조 포맷으로 요청`

* :ref:`Geo filtering <geofilter>` 돌발 정보 탐색하고자 하는 지리적 영역 규정 (`filter_type`)
* 획득 하고자 하는 정보의 유형 및 카테고리 선택 (`incidentField`, `type`)
* 위치 참조 방식 선택 (`lr`)

:underline:`Request Example`

.. code-block:: none

  ruut/v1/incidents?filter_type=circle&center=37.397619, 127.112465&radius=100&frc=1
  &incidentField=all&type=all&lr=all


V2X 서비스 연동 요청 
--------------------------

작성 중


과거 교통 정보 요청
--------------------------

작성 중

