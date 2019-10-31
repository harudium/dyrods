메시지 포맷
=======================================

.. rst-class:: table-width-fix

.. _message_formats:

RUUT의 메세지는 크게 3가지로 구분됩니다. 
* Segment : Segment 기반의 실시간 교통 정보 메시지
* Incident : Segment 기반의 이벤트 (사고/공사 등) 정보 메시지
* TPEG : TPEG2 TFP/TEC/WEA 어플리케이션 Binary 또는 TPEG-ML 메시지

.. _segment_formats:

Segment
----------------
RUUT 는 지도 형태 독립적으로 도로를 관리합니다. 이에 교통 정보를 더 효율적으로 관리할 수 있도록 별도의 도로 링크 형태를 활용하며 이를 시스템 내에서 Segment라 부릅니다.하나의 Segment는 시작 노드(Start Node)와 종료 노드(End Node)를 가진 선형 링크(Linear Link)이며, RUUT 의 모든 기본 정보 제공 단위는 Segment이며 해당 Segment를 활용한 맵 매칭을 위해서 openLR, AGORA-C 와 같은 Dynamic Location Referencing 기법에 따른 위치 참조 코드를 제공하고 있습니다. Dynamic Location Referencing 기법을 활용하기 어려운 light 사용자를 위하여 Segment의 시작/끝 지점에 대한 GPS 좌표를 동시에 제공하고 있습니다.

RUUT 를 구성하는 가장 기본 구성 단위이기 때문에 Segment 를 endpoint 로 하는 API 요청 응답은 Segment 기반으로 실시간/예측 교통 정보를 전달하고 해당 메시지 포맷은 아래 코드 블록과 같습니다.

**Segment 메시지 응답**

.. code-block:: json

    {
      "segments": [{
        "segmentId": "ID of the filtered segment",
        "roadCate": "FRC number of the road on the segment",
        "speed": "current speed of the segment",
        "limit": "speed limit of the segment",
        "freeflow": "free flow speed of the segment",
        "travelTime": "estimated time to traverse the segment",
        "openLR": "openLR code of the segment",
        "agoraC": "AGORA-C code of the segment",
        "gps-coordinates": "gps coordinates of the start/end node of the segment",

        // only for predict response
        "confidenceLevel": "Level of confidence of the traffic prediction",

        // only if when the data is exist
        "lane": [{
          "laneNumber": "Lane number",
          "laneSpeed": "dedicated speed of the lane on the segment"
        }],
        "timeStamp": "timestamp of the information"
      }]
    }


Incident
---------------------
Incident 는 도로 위 이벤트 정보 즉, 사고, 재해, 공사, 행사 등의 정보를 다룹니다. 나머지 내용은 :ref:`Segment 포맷 <segment_formats>`과 동일 합니다.

**Incident 메시지 응답**

.. code-block:: json

  {
    "incidents": [{
      "segmentId": "ID of the segment where the events are occurred",
      "incidentId": "ID of the incident",
      "incidentType": "type of the incident",
      "severity": "severity of the incident",
      "impacting": "whether the incident has an impact to traffic flow",
      "status": "incident status",
      "lane": "lane number of the event",
      "length": "length of the incident has occurred",
      "vehicleKind": "이게 뭘까요?",
      "description": "detail explanation of the incident",
      "schedule": {
        "isPlanned": "whether the event is planned of not",
        "startTime": "start time of the event (only if scheduled)",
        "endTime": "end time of the event (only if scheduled)",
        "reoccuring":{
          "daysOfWeek": "days when the event is re-occurred",
          "from": "start time of the upcoming event",
          "until": "end time of the upcomfing event"
        }
       },
      "openLR": "openLR code of the segment",
      "agoraC": "AGORA-C code of the segment",
      "timeStamp": "timestamp of the information"
    }]
  }


TPEG
---------------------
