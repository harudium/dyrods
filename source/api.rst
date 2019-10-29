API 규격
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
