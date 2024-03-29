API 규격
=======================================

.. rst-class:: table-width-fix

.. _apidoc:

**Endpoint**

- RUUT 교통 정보 : `/ruut/version/segments`
- RUUT 이벤트 정보 : `/ruut/version/incidents`
- RUUT TPEG : `/ruut/version/tpeg`

.. _geofilter:

Geo Filtering
--------------------------

지도 상의 영역을 지정하고 해당 영역 내에 포함되는 데이터만 추출하는 데 사용합니다. 인증, V2X를 제외한 모든 RUUT 플랫폼 기능의 필수 파라미터 입니다. Geo Filtering 은 총 5개 종류가 제공되며 각각의 필터 타입을 규정하기 위한 파라미터를 병용 하여야 합니다. 

Geo Filtering 파라미터 리스트
''''''''''''''''''''''''''

5개의 필터는 `filter-type` 파라미터의 값 영역에 명시하여 활성화 할 수 있습니다. 각각의 필터는 동시 사용이 불가합니다. 또한, 해당 필터와 병용 되어야 하는 파라미터가 추가로 명시되지 않을 경우 필터가 정상 동작하지 않습니다.

.. note:: 예) `/endpoint?filter-type=box&corner1={gps}&corner2={gps}` *`box` should be combined with `corner1` and `corner2`
=============  =========  =================  ========================================================
Params           Type         Value              Description
=============  =========  =================  ========================================================
filter-type    String     box                2개 gps 좌표로 이루어진 사각 영역 필터링
-------------  ---------  -----------------  --------------------------------------------------------
\              \          circle             중심 좌표(gps)와 반지름 으로 이루어진 원 영역 필터링 
-------------  ---------  -----------------  --------------------------------------------------------
\              \          polygon            3개 이상의 gps 좌표로 이루어진 다각형 영역 필터링 (8개 좌표 이내)
-------------  ---------  -----------------  --------------------------------------------------------
\              \          pos                1개 gps 좌표에서 가장 가까운 세그먼트 필터링 (250미터 이내)
-------------  ---------  -----------------  --------------------------------------------------------
\              \          centerpoint-box    1개 gps 좌표를 무게중심으로 하는 사각형 영역 필터링
-------------  ---------  -----------------  --------------------------------------------------------
corner1        String     gps 좌표            `box` 필터의 대각 gps 좌표 (`corner2` 와 쌍)
-------------  ---------  -----------------  --------------------------------------------------------
corner2        String     gps 좌표            `box` 피렅의 대각 gps 좌표 (`corner1` 과 쌍)
-------------  ---------  -----------------  --------------------------------------------------------
center         String     gps 좌표            `circle` or `centerpoint-box` 필터의 중심 좌표
-------------  ---------  -----------------  --------------------------------------------------------
radius         Integer    radius             `circle` 필터의 반지름 (미터)
-------------  ---------  -----------------  --------------------------------------------------------
height         Integer    height             `centerpoint-box` 필터의 세로 값 (미터)
-------------  ---------  -----------------  --------------------------------------------------------
width          Integer    width              `centerpoint-box` 필터의 가로 값 (미터)
-------------  ---------  -----------------  --------------------------------------------------------
points         String     gps 좌표 리스트       `polygon` 필터의 gps 좌표. 파이프 기호로 구분된 목록
-------------  ---------  -----------------  --------------------------------------------------------
point          String     gps 좌표            `pos` 필터의 gps 좌표
-------------  ---------  -----------------  --------------------------------------------------------
regionId       Integer    지역코드              행정 구역 단위 필터링을 위한 지역 코드 [#]_
=============  =========  =================  ========================================================

Geo Filtering 제한 사항
''''''''''''''''''''''''''
Geo filtering 은 파라미터 규칙 외 필터 성능 최적화 및 사용성 강화를 위한 제한 사항이 포함 됩니다. 

* 탐색을 요청하는 도로 등급에 따라 제한이 적용 됩니다 (`circle/box` 필터 기준)
 - FRC 레벨 == 0 (고속도로) : 반지름 및 가로/세로 200km 이내 제한
 - 0 < FRC 레벨 < 3 (국도, 고속화도로) : 반지름 및 가로/세로 100km 이내 제한
 - 2 < FRC 레벨 (모든 도로) : 반지름 및 가로/세로 20km 이내 제한

해당 제한을 따르지 않은 요청에 대해서는 정상 응답을 하지 않으니 이에 유의 하시기 바랍니다 (오류 응답)


Geo Filtering 예제 
''''''''''''''''''''''''''
Geo filter 는 모든 교통 정보 데이터 검색 요청의 필수 요소 입니다. 아래에 나온 필터의 종류에 따른 URL sample 을 참고하여 원하는 영역에 대한 필터링 조건을 설정하고 해당 URL 의 뒤에 세부 요청 파라미터를 추가하는 형태로 API 호출이 진행 됩니다. 

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
| centerpoint-box | **GET** | `/endpoint?filter-type=centerpoint-box&center={gps}&height={km}`\\   |
|                 |         | `&length={km}`                                                       | 
+-----------------+---------+----------------------------------------------------------------------+


RUUT
--------------------------
RUUT 플랫폼에서 자체적으로 제공하고 있는 API 구성을 설명 합니다. RUUT API 는 크게 Segement 와 Incident 로 구성 되어 있습니다. Segement 는 실시간 교통 정보 및 예측 교통 정보 검색에 사용되며, Incident 는 실시간 이벤트 (사고, 공사, 재해 등) 검색에 사용됩니다. TPEG2 데이터 검색은 TPEG2 섹션을 참고 하시기 바랍니다.

Segment
''''''''''''''''''''''''''
RUUT API 의 path 파라미터로 사용되는 segment 는 실시간 또는 예측 교통 정보를 요청 하기 위해 사용 됩니다. 해당 교통 정보에 이벤트 (사고, 재해, 공사등)정보는 포함되지 않습니다. 이벤트 정보는 아래 incident 를 참조하시기 바랍니다. 

**Segment Request**

+------------+-------------------------------------------------------------------------------------+
| **GET**    | `/ruut/{version}/segments?{geo-query}?{set of parameters}`                          |
+------------+-------------------------------------------------------------------------------------+

RUUT API 에 대한 요청은 위와 같은 URL로 구성 됩니다. 앞서 언급한 바와 같이 goe filter 를 먼저 URL 에 추가한 후 아래 Request Parameters 를 추가 입력하면 됩니다.

Segment Request Parameters
..........................

=============  =========  =================  ========================================================
Params           Type         Value              Description
=============  =========  =================  ========================================================
rttiField       String        speed          현재 측정 속도 반환
-------------  ---------  -----------------  --------------------------------------------------------
\                \           limit           세그먼트 제한 속도 반환 
-------------  ---------  -----------------  --------------------------------------------------------
\                \           travletime      세그먼트 횡단 평균 시간 반환
-------------  ---------  -----------------  --------------------------------------------------------
\                \           freeflow        정체 없을 시 속도 반환
-------------  ---------  -----------------  --------------------------------------------------------
\                \           all(default)    모든 필드 반환
-------------  ---------  -----------------  --------------------------------------------------------
frc             Integer     frc              FRC 등급이 같은 항목만 반환 (쉼표 나누어 여러 개의 등급 명시 가능)
-------------  ---------  -----------------  --------------------------------------------------------
\                \          all(default)     모든 FRC 등급 데이터 반환
-------------  ---------  -----------------  --------------------------------------------------------
start-time      Datetime    yyyymmddhhss     해당 시점 데이터 반환하며 시점에 따라 3가지 패턴으로 구분

                                             - 현재
                                             - 과거
                                             - 미래
-------------  ---------  -----------------  --------------------------------------------------------
duration        Integer    5 - 60            start-time 부터 duration 까지의 데이터 반환. 예측 데이터의 
                                             경우 현재 시간 대비 1시간 까지만 반환 가능 
-------------  ---------  -----------------  --------------------------------------------------------
interval        Integer    분                 과거/미래 데이터 요청 시 매 `interval` 마다 데이터 추출
-------------  ---------  -----------------  --------------------------------------------------------
lane            String     on (default)      차선 단위 교통 정보 활성화
\                 \        off               차선 단위 교통 정보 비활성화
-------------  ---------  -----------------  --------------------------------------------------------
lr              String     openlr            위치 참조 정보로 openLR 인코딩 정보 반환
\                 \        agorac            위치 참조 정보로 AGORA-C 인코딩 정보 반환
\                 \        all (default)     위치 참조 정보로 openLR / AGORA-C 인코딩 정보 반환
-------------  ---------  -----------------  --------------------------------------------------------
coordinates     String     on (default)      제공 세그먼트의 시작/끝 노드의 GPS 좌표 정보 반환
\                 \        off               세그먼트 GPS 정보 반환 않음
=============  =========  =================  ========================================================

Segment Response Parameters
..........................

.. note:: 응답은 하나 이상의 segment 로 구성 되며 JSON array 형태로 구성 됩니다.

================  =========  ===========================================================================
Property          Type       Description
================  =========  ===========================================================================
segmentid         String     세그먼트의 ID
----------------  ---------  ---------------------------------------------------------------------------
roadcate          String     세그먼트의 도로 레벨
----------------  ---------  ---------------------------------------------------------------------------
speed             Integer    세그먼트의 측정 차량 속도
----------------  ---------  ---------------------------------------------------------------------------
limit             Integer    세그먼트의 제한 속도
----------------  ---------  ---------------------------------------------------------------------------
freeflow          Integer    세그먼트 정체 없을 경우 차량 평균 속도
----------------  ---------  ---------------------------------------------------------------------------
traveltime        String     세그먼트를 관통 하는데 걸리는 시간 (초)
----------------  ---------  ---------------------------------------------------------------------------
openLR            String     위치 참조를 위한 openLR encoded code
----------------  ---------  ---------------------------------------------------------------------------
agoraC            String     위치 참조를 위한 AGORA-C encoded code
----------------  ---------  ---------------------------------------------------------------------------
confidenceLevel   String     예측 신뢰도 (에측 데이터일 경우에만 제공)
----------------  ---------  ---------------------------------------------------------------------------
lane              Array      차선 교통 정보 제공을 위한 배열 객체
----------------  ---------  ---------------------------------------------------------------------------
ㄴ laneNumber      String     차선 번호 (안쪽 차선부터 1차선)
----------------  ---------  ---------------------------------------------------------------------------
ㄴ laneSpeed       Integer    `laneNumber`로 특정된 차선의 측정 속도
----------------  ---------  ---------------------------------------------------------------------------
timeStamp         Datetime   정보 생성 시간 
================  =========  ===========================================================================

Segment Request/Response Example
..........................
**Request Example**

+------------+-------------------------------------------------------------------------------------+
| **GET**    | `{host-ip}/ruut/v1/segments?filter_type=circle&center=37.397619,%20127.112465`      |
|            | `&radius=10&frc=1&rttiField=all&regionId=0&lr=all&lane=on`                          |
+------------+-------------------------------------------------------------------------------------+

**Response Example**

.. code-block:: json

    {
      "segments": [{
        "segmentId": "1020174101",
        "roadCate": 1,
        "speed": "84",
        "limit": "80",
        "freeFlow": "80",
        "travelTime": "58",
        "openLR": "C1pdVxqjGwktFgCN+34JEQ==",
        "agoraC": "",
        "lane": [
            {
                "laneNumber": "",
                "laneSpeed": ""
            }
        ],
        "timeStamp": "2019-10-23 15:04:00"
      }]
    }

Incident
''''''''''''''''''''''''''
RUUT API 의 path 파라미터로 사용되는 incident 는 도로 상의 이벤트인 사고, 재해, 공사, 일정, 통제 정보를 제공 합니다. 앞서 설명된 segment 와 마찬가지로 incident 의 query 파라미터 또한 Geo filtering 파라미터와 더불어 사용 됩니다.

**Incident Request**

+------------+-------------------------------------------------------------------------------------+
| **GET**    | `/ruut/{version}/incidents?{geo-query}?{set of parameters}`                          |
+------------+-------------------------------------------------------------------------------------+

RUUT API 에 대한 요청은 위와 같은 URL로 구성 됩니다. 앞서 언급한 바와 같이 goe filter 를 먼저 URL 에 추가한 후 아래 Request Parameters 를 추가 입력하면 됩니다.

Request Parameters (incident)
................................

=============  =========  =================  ========================================================
Params           Type         Value              Description
=============  =========  =================  ========================================================
incidentField  String     severity           이벤트 심각도 (제공 예정) 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          impacting          이벤트가 세그먼트의 교통 흐름에 영향을 미치는지 여부 (제공 예정) 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          status             이벤트의 지속 상태 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          lane               이벤트 발생 차선 정보 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          length             이벤트가 영향을 미치는 물리적 범위 (미터) 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          vehicleKind        이벤트 차량 종류 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          description        이벤트 세부 정보 문자열 반환
-------------  ---------  -----------------  --------------------------------------------------------
\              \          all(default)       모든 필드 반환
-------------  ---------  -----------------  --------------------------------------------------------
start-time      Datetime    yyyymmddhhss     과거 데이터 요청 시점 명시 용도
-------------  ---------  -----------------  --------------------------------------------------------
duration        Integer    5 - 60            과거 데이터 요청 시 start-time 부터 duration 까지 데이터 반환
-------------  ---------  -----------------  --------------------------------------------------------
interval        Integer    분                 과거 데이터 요청 시 매 `interval` 마다 데이터 추출
-------------  ---------  -----------------  --------------------------------------------------------
lr              String     openlr            위치 참조 정보로 openLR 인코딩 정보 반환
\                 \        agorac            위치 참조 정보로 AGORA-C 인코딩 정보 반환
\                 \        all (default)     위치 참조 정보로 openLR / AGORA-C 인코딩 정보 반환
-------------  ---------  -----------------  --------------------------------------------------------
coordinates     String     on (default)      제공 세그먼트의 시작/끝 노드의 GPS 좌표 정보 반환
\                 \        off               세그먼트 GPS 정보 반환 않음
=============  =========  =================  ========================================================

Response Parameters
..........................

.. note:: 응답은 하나 이상의 segment 로 구성 되며 JSON array 형태로 구성 됩니다.

================  =========  ===========================================================================
Property          Type       Description
================  =========  ===========================================================================
segmentId         String     세그먼트의 ID
----------------  ---------  ---------------------------------------------------------------------------
incidentId        String     이벤트의 ID
----------------  ---------  ---------------------------------------------------------------------------
incidentType      String     이벤트의 타입 (A:사고, B:공사, C:행사, D:재해, E:통제)
----------------  ---------  ---------------------------------------------------------------------------
severity          Integer    이벤트의 심각도 (제공 예정)
----------------  ---------  ---------------------------------------------------------------------------
impacting         Integer    이벤트가 주변 교통에 영향을 끼치는 정도 (제공 예정)
----------------  ---------  ---------------------------------------------------------------------------
status            Integer    이벤트 진행 상태 
----------------  ---------  ---------------------------------------------------------------------------
lane              Integer    이벤트 발생 차선 정보
----------------  ---------  ---------------------------------------------------------------------------
vehicleKind       String     사고 차량 종류
----------------  ---------  ---------------------------------------------------------------------------
description       String     이벤트 세부 정보 설명 문자열 
----------------  ---------  ---------------------------------------------------------------------------
schedule          Object     이벤트에 일정에 있을 때 제공되는 오브젝트 (이벤트 일정이 있는 경우에만 기본 제공)
----------------  ---------  ---------------------------------------------------------------------------
ㄴ isPlanned       String     계획된 이벤트인지 여부
----------------  ---------  ---------------------------------------------------------------------------
ㄴ startTime       Datetime   이벤트 개시 시점
----------------  ---------  ---------------------------------------------------------------------------
ㄴ endTime         Datetime   이벤트 종료 시점
----------------  ---------  ---------------------------------------------------------------------------
ㄴ reoccuring      Object     반복 이벤트인지 여부에 따라 제공되는 오브젝트 
----------------  ---------  --------------------------------------------------------------------------- 
ㄴ daysOfWeek      String     일주일 중 언제 반복 발생하는지
----------------  ---------  ---------------------------------------------------------------------------
ㄴ from            String     반복 이벤트 시작 시점
----------------  ---------  ---------------------------------------------------------------------------
ㄴ until           String     반복 이벤트 종료 시점
----------------  ---------  ---------------------------------------------------------------------------
openLR            String     위치 참조를 위한 openLR encoded code
----------------  ---------  ---------------------------------------------------------------------------
agoraC            String     위치 참조를 위한 AGORA-C encoded code
----------------  ---------  ---------------------------------------------------------------------------
timeStamp         Datetime   정보 생성 시간 
================  =========  ===========================================================================

Request/Response Example
..........................
**Request Example**

+------------+--------------------------------------------------------------------------------------+
| **GET**    | `{host-ip}/ruut/:version/incidents?filter_type=circle&center=37.397619, 127.112465&` |
|            | `radius=100&frc=1&incidentField=all&type=all&lr=all`                                 |
+------------+--------------------------------------------------------------------------------------+

**Response Example**

.. code-block:: json

    "incidents": [
        {
            "segmentId": "1020004101",
            "incidentId": "L93105079001",
            "incidentType": "B",
            "severity": "",
            "impacting": "",
            "status": "",
            "lane": "00",
            "length": 188,
            "vehicleKind": "000000",
            "description": "<경찰청제공>[공사] 올림픽대로 가양대교 에서 방화대교 방향 3차로 도로공사 / 공사명 : 2019년 자동차전용도로 강남배수시설물 준설 및 정비공사 (연간단가) / 장소 : 올림픽대로램프 88JC / 부분통제",
            "schedule": {
                "isPlanned": "",
                "startTime": "201910182300",
                "endTime": "201910260600",
                "reoccuring": {
                    "daysOfWeek": "",
                    "from": "",
                    "until": ""
                }
            },
            "openLR": "C1os2xq6/gkqFwUd/XQJCg==",
            "agoraC": "",
            "timeStamp": "2019-10-23 15:04:00"
        }

RUUT TPEG
--------------------------
RUUT는 자체적으로 TPEG2 표준에 맞는 교통 데이터를 제공하고 있습니다. TPEG2는 기존 TPEG 대비하여 제공 데이터의 정밀도 향상, 교통 정보 범위 확대, 차선 단위 교통정보 제공 기능 추가, 예측 교통 정보 제공을 위한 포맷 강화, Peer to Peer 연동 규격 추가 등을 제공하는 최신 교통 정보 제공 국제 표준입니다. RUUT TPEG2 는 TPEG2 어플리케이션 중 아래 3가지 어플리케이션을 제공합니다.

* TFP : 실시간 교통 정보
* TEC : 실시간 이벤트(돌발) 정보
* WEA : 날씨 정보

TPEG2
''''''''''''''''''''''''''

**TPEG2 Request**

+------------+-------------------------------------------------------------------------------------+
| **GET**    | `/ruut/{version}/tpeg/getMessage?{geo-query}?{set of parameters}`                   |
+------------+-------------------------------------------------------------------------------------+

RUUT TPEG 메시지에 대한 요청은 위와 같은 URL로 구성 됩니다. 앞서 언급한 바와 같이 goe filter 를 먼저 URL 에 추가한 후 아래 Request Parameters 를 추가 입력하면 됩니다.

Request Parameters (TPEG2)
................................

=============  =========  ===================  ========================================================
Params           Type         Value                Description
=============  =========  ===================  ========================================================
frc            Integer    frc                  FRC 등급이 같은 항목만 반환 (쉼표 나누어 여러 개의 등급 명시 가능)
-------------  ---------  -------------------  --------------------------------------------------------
\              \          all (default)        모든 FRC 등급 데이터 반환
-------------  ---------  -------------------  --------------------------------------------------------
format         String     base64xml (default)  TPEG 메시지를 base64 로 인코딩 한 후 xml 컨테이너로 반환
\              \          tepgML               TPEG 메시지를 TPEG-ML 로 반환
-------------  ---------  -------------------  --------------------------------------------------------
app            String     tfp (default)        TPEG2 TFP 어플리케이션 반환
\              \          tec                  TEPG2 TEC 어플리케이션 반환
\              \          wea                  TEPG2 WEA 어플리케이션 반환
-------------  ---------  -------------------  --------------------------------------------------------
delta          String     on                   이전 요청에서 변경된 데이터만 반환 (델타 업데이트)
\              \          off                  매 요청 시 모든 세그먼트 데이터 반환 (전체 업데이트)
=============  =========  ===================  ========================================================

Response Formats (TPEG2)
..........................

TEPG2 요청에 대한 응답은 2 가지 형태로 제공 됩니다.
* TPEG2 Message Binary > Base64 Encoding > XML container
* TPEG2 ML

각 응답 포맷에 대한 세부 사항은 TPEG2 표준 문서를 참고 하시기 바랍니다.

Request/Response Example
..........................
**Request Example**

+------------+--------------------------------------------------------------------------------------+
| **GET**    | `{host-ip}/ruut/:version/tpeg/getMessage?filter_type=circle&center=37.521523,`       | 
|            | `127.017932&radius=0.5&app=tfp&format=tpegML&frc=0&fullUpdate=on`                    |
+------------+--------------------------------------------------------------------------------------+

**Response Example**

.. code-block:: xml

	<ApplicationRootMessage>
        <ApplicationRootMessageML xsi:type="tfp:TFPMessage" xmlns:tfp="http://www.tisa.org/TPEG/TFP_1_0">
            <tfp:mmt>
                <tfp:optionMessageManagement>
                    <mmc:messageID>53745</mmc:messageID>
                    <mmc:versionID>12</mmc:versionID>
                    <mmc:messageExpiryTime>1970-01-01T00: 00: 00Z</mmc:messageExpiryTime>
                    <mmc:cancelFlag>false</mmc:cancelFlag>
                    <mmc:messageGenerationTime>2019-10-23T05: 52: 00Z</mmc:messageGenerationTime>
                </tfp:optionMessageManagement>
            </tfp:mmt>
            <tfp:method xsi:type="tfp:FlowStatus">
                <tfp:startTime>1970-01-01T00: 00: 00Z</tfp:startTime>
                <tfp:duration>0</tfp:duration>
                <tfp:status>
                    <tfp:LOS tfp:code="2" tfp:table="tfp003_LevelOfService"/>
                    <tfp:averageSpeed>60</tfp:averageSpeed>
                    <tfp:freeFlowTravelTime>80</tfp:freeFlowTravelTime>
                </tfp:status>
                <tfp:restriction>
                    <tfp:lanes tfp:code="0" tfp:table="tfp005_laneRestriction"/>
                </tfp:restriction>
                    <tfp:cause tfp:code="0" tfp:table="tfp006_CauseCode"/>
                <tfp:detailedCause>
                    <tfp:messageID>53745</tfp:messageID>
                    <tfp:COID>0</tfp:COID>
                </tfp:detailedCause>
            </tfp:method>
            <tfp:loc>00000000380000003801005A52851AAD88000900000005000000050000010C000A00000004000000040502FE0000CC027600090000000500000005050003ED0000</tfp:loc>
        </ApplicationRootMessageML>
    </ApplicationRootMessage>

Auxiliary
--------------------------
History
''''''''''''''''''''''''''

Errors
--------------------------
RUUT API 호출 중 발생하는 에러 코드에 대한 안내


.. [#] 행정 구역 코드는 별도로 안내.