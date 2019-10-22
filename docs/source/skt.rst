RUUT 서비스 가이드
=======================================

.. _general_authentication:
인증 (공통 프로세스)
--------------------------
계정 생성
''''''''''''''''''''''''''
API 호출을 통해 계정을 생성 합니다.

.. rst-class:: table-width-fix
.. rst-class:: text-align-justify

+------------+------------------------------------+
| **POST**   | `/api/auth/join`.                  |
+------------+------------------------------------+

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

.. rst-class:: table-width-full
.. rst-class:: text-align-justify

+----------+--------+-------------------------+
| body row 1 | column 2   | column 3   | 
+------------+------------+-----------+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 

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

.. code-block:: json

    {
        "token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXNhZG1pbkB0aG…",
        "refreshToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXNhZG1…"
    }

.. rst-class:: text-align-justify

로그인 (인증 토큰 획득)
''''''''''''''''''''''''''
토큰 갱신
''''''''''''''''''''''''''
패스워드 변경
''''''''''''''''''''''''''
패스워드 리셋
''''''''''''''''''''''''''


JSON 응답 교통 정보 요청
--------------------------
실시간 교통 정보
''''''''''''''''''''''''''
예측 교통 정보
''''''''''''''''''''''''''
실시간 교통 정보
''''''''''''''''''''''''''

V2X 서비스 연동 요청 
--------------------------

과거 교통 정보 요청
--------------------------

