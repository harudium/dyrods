메시지 포맷
=======================================

.. rst-class:: table-width-fix

.. _message_formats:

.. code-block:: json
    :linenos:

    {
      "segments": [
      {
        "segmentId": "ID of the filtered segment",
        "roadCate": "FRC number of the road on the segment",
        "speed": "current speed of the segment",
        "limit": "speed limit of the segment",
        "freeflow": "free flow speed of the segment",
        "travelTime": "estimated time to traverse the segment",
        "openLR": "openLR code of the segment",
        "agoraC": "AGORA-C code of the segment",
        "confidenceLevel": "Level of confidence of the traffic prediction",
        "lane": [
        {
          "laneNumber": "Lane number",
          "laneSpeed": "dedicated speed of the lane on the segment"
        }
        ],
        "timeStamp": "timestamp of the information"
      }
      ]
    }


세그먼트 (Segment)
================

RUUT 는 지도 형태 독립적으로 도로를 관리합니다. 이에 교통 정보를 더 효율적으로 관리할 수 있도록 별도의 도로 링크 형태를 활용하며 이를 시스템 내에서 세그먼트 (Segment)라 부릅니다.하나의 세그먼트는 시작 노드(Start Node)와 종료 노드(End Node)를 가진 선형 링크(Linear Link)이며, RUUT 의 모든 기본 정보 제공 단위는 세그먼트이며 해당 세그먼트를 활용한 맵 매칭을 위해서 openLR, AGORA-C 와 같은 Dynamic Location Referencing 기법에 따른 위치 참조 코드를 제공하고 있습니다. Dynamic Location Referencing 기법을 활용하기 어려운 light 사용자를 위하여 세그먼트의 시작/끝 지점에 대한 GPS 좌표를 동시에 제공하고 있으니 참고 하시기 바랍니다. 

