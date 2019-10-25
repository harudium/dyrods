메시지 포맷
=======================================

.. rst-class:: table-width-fix

.. _message_formats:

**Endpoint**

- RUUT 교통 정보 : `/ruut/version/segments`
- RUUT 이벤트 정보 : `/ruut/version/incidents`
- RUUT TPEG : `/ruut/version/tpeg`

Geo Filtering
--------------------------

지도 상의 영역을 지정하고 해당 영역 내에 포함되는 데이터만 추출하는 데 사용합니다. 인증, V2X를 제외한 모든 RUUT 플랫폼 기능의 필수 파라미터 입니다. Geo Filtering 은 총 5개 종류가 제공되며 각각의 필터 타입을 규정하기 위한 파라미터를 병용 하여야 합니다. 

Geo Filtering 파라미터 리스트
''''''''''''''''''''''''''

5개의 필터는 `filter-type` 파라미터의 값 영역에 명시하여 활성화 할 수 있습니다. 각각의 필터는 동시 사용이 불가합니다. 또한, 해당 필터와 병용 되어야 하는 파라미터가 추가로 명시되지 않을 경우 필터가 정상 동작하지 않습니다.

.. note:: 예) `/endpoint?filter-type=box&corner1={gps}&corner2={gps}` *`box` should be combined with `corner1` and `corner2`

+-------------+---------+-----------------+--------------------------------------------------------+
| Params      | Type    | Value           | Description                                            |
+=============+=========+=================+========================================================+
| filter-type | String  | box             | box shaped filter with 2 gps coordinates               |
+             +         +-----------------+--------------------------------------------------------+
|             |         | circle          | circle shaped filter with a centerpoint and a radius   |
+             +         +-----------------+--------------------------------------------------------+
|             |         | polygon         | polygon shaped filter with 3+ gps coordinates          |
+             +         +-----------------+--------------------------------------------------------+
|             |         | pos             | get the closest data from the position                 |
+             +         +-----------------+--------------------------------------------------------+
|             |         | centerpoint-box | box shaped filter with 1 center, width, height         |
+-------------+---------+-----------------+--------------------------------------------------------+
| corner1     | String  | gps             | diagonal point 1 of the 'box' filter                   |
+-------------+---------+-----------------+--------------------------------------------------------+
| corner2     | String  | gps             | diagonal point 2 of the 'box' filter                   |
+-------------+---------+-----------------+--------------------------------------------------------+
| center      | String  | gps             | centerpoint of the `circle` or `centerpoint-box` filter|
+-------------+---------+-----------------+--------------------------------------------------------+
| radius      | Integer | radius          | radius(km) of the `circle` filter                      |
+-------------+---------+-----------------+--------------------------------------------------------+
| height      | Integer | box height      | height (km) of the `centerpoint-box` filter            |
+-------------+---------+-----------------+--------------------------------------------------------+
| width       | Integer | box width       | width (km) of the `centerpoint-box` filter             |
+-------------+---------+-----------------+--------------------------------------------------------+
| points      | String  | gps             | A pipe-delimeted list of gps coordinates of            |
|             |         |                 | `polygon` filter. Max 8 coordinates are allowed        |
+-------------+---------+-----------------+--------------------------------------------------------+
| point       | String  | gps             | gps point to get the closest one by the `pos` filter   |
+-------------+---------+-----------------+--------------------------------------------------------+
| regionid    | Integer | region ID       | region ID to filter by administrative area             |
+-------------+---------+-----------------+--------------------------------------------------------+

Geo Filtering 예제 
''''''''''''''''''''''''''
+-----------------+---------+----------------------------------------------------------------------+
| Filter          | Method  | URL Sample                                                           |
+=================+=========+======================================================================+
| box             | **GET** | `/endpoint?filter-type=box&corner1={gps}&corner2={gps}`              |
+-----------------+---------+----------------------------------------------------------------------+
| circle          | **GET** | `/endpoint?filter-type=circle&center={gps}&radius={km}`              |
+-----------------+---------+----------------------------------------------------------------------+
| polygon         | **GET** | `/endpoint?filter-type=polygon&points={gps}|{gps}|{gps}|...`         |
+-----------------+---------+----------------------------------------------------------------------+
| pos             | **GET** | `/endpoint?filter-type=pos&point={gps}`                              |
+-----------------+---------+----------------------------------------------------------------------+
| centerpoint-box | **GET** | `/endpoint?filter-type=centerpoint-box&center={gps}&height={km}`     |
|                 |         | `&length={km}`                                                       | 
+-----------------+---------+----------------------------------------------------------------------+



RUUT
--------------------------
Segment
''''''''''''''''''''''''''
**Request**

Request URL

Parameters
+-------------+--------+-----------------+--------------------------------------------------------+
| Params      | Type   | Value           | Description                                            |
+=============+========+=================+========================================================+
| filter-type | String | box             | box shaped filter with 2 gps coordinates               |
+-------------+--------+-----------------+--------------------------------------------------------+

**Response**

Incident
''''''''''''''''''''''''''

RUUT TPEG
--------------------------
TPEG2
''''''''''''''''''''''''''

Auxiliary
--------------------------
History
''''''''''''''''''''''''''
