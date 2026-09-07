# final-R1: 100건 전체 결과

각 JSON은 순서가 있는 전체 후보·중간 순위·점수·평가·시간을 보존한다. context는 원문을 중복 인쇄하는 대신 [전체 청크](CHUNK-CATALOG.md)의 ID로 연결한다. 원시 JSONL에는 반환 원문도 모두 들어 있다.

## Q001

구독 날짜와 시각은 어느 나라 시간 기준인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-COMMON-001",
      "anchor": "KST",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 146,
          "quote": "- 정책 내용: 구독·결제·주문에 사용하는 날짜와 시각은 대한민국 표준시인 KST를 기준으로 계산한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q001",
  "group": "G001",
  "question": "구독 날짜와 시각은 어느 나라 시간 기준인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.69569999910891,
  "retrievalMs": 3.64120000085677,
  "hits": [
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "denseScore": 0.8770462870597839,
      "score": 0.8770462870597839
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "denseScore": 0.8770164251327515,
      "score": 0.8770164251327515
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.8720882534980774,
      "score": 0.8720882534980774
    },
    {
      "chunkId": "knowledge-1-123988be5b9322c3578cb7a22d6aedcc8f920acc85cf4a958843c1fbfc5ba84d",
      "denseScore": 0.867754340171814,
      "score": 0.867754340171814
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.8667689561843872,
      "score": 0.8667689561843872
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "denseScore": 0.8770462870597839,
      "score": 0.8770462870597839
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "denseScore": 0.8770164251327515,
      "score": 0.8770164251327515
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.8720882534980774,
      "score": 0.8720882534980774
    },
    {
      "chunkId": "knowledge-1-123988be5b9322c3578cb7a22d6aedcc8f920acc85cf4a958843c1fbfc5ba84d",
      "denseScore": 0.867754340171814,
      "score": 0.867754340171814
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.8667689561843872,
      "score": 0.8667689561843872
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
        "denseScore": 0.8770462870597839,
        "score": 0.8770462870597839
      },
      {
        "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
        "denseScore": 0.8770164251327515,
        "score": 0.8770164251327515
      },
      {
        "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
        "denseScore": 0.8720882534980774,
        "score": 0.8720882534980774
      },
      {
        "chunkId": "knowledge-1-123988be5b9322c3578cb7a22d6aedcc8f920acc85cf4a958843c1fbfc5ba84d",
        "denseScore": 0.867754340171814,
        "score": 0.867754340171814
      },
      {
        "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
        "denseScore": 0.8667689561843872,
        "score": 0.8667689561843872
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 525,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-COMMON-001",
        "anchor": "KST",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "originHit": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1"
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "originHit": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4"
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "originHit": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26"
    },
    {
      "chunkId": "knowledge-1-123988be5b9322c3578cb7a22d6aedcc8f920acc85cf4a958843c1fbfc5ba84d",
      "originHit": "knowledge-1-123988be5b9322c3578cb7a22d6aedcc8f920acc85cf4a958843c1fbfc5ba84d"
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "originHit": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd"
    }
  ]
}
```

## Q002

결제 시간 안내는 한국 표준시로 보면 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-COMMON-001",
      "anchor": "KST",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 146,
          "quote": "- 정책 내용: 구독·결제·주문에 사용하는 날짜와 시각은 대한민국 표준시인 KST를 기준으로 계산한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q002",
  "group": "G001",
  "question": "결제 시간 안내는 한국 표준시로 보면 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.481000000960194,
  "retrievalMs": 3.8538999997399515,
  "hits": [
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.85459303855896,
      "score": 0.85459303855896
    },
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "denseScore": 0.851176917552948,
      "score": 0.851176917552948
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "denseScore": 0.8500742316246033,
      "score": 0.8500742316246033
    },
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "denseScore": 0.8500374555587769,
      "score": 0.8500374555587769
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.8494212627410889,
      "score": 0.8494212627410889
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.85459303855896,
      "score": 0.85459303855896
    },
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "denseScore": 0.851176917552948,
      "score": 0.851176917552948
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "denseScore": 0.8500742316246033,
      "score": 0.8500742316246033
    },
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "denseScore": 0.8500374555587769,
      "score": 0.8500374555587769
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.8494212627410889,
      "score": 0.8494212627410889
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
        "denseScore": 0.85459303855896,
        "score": 0.85459303855896
      },
      {
        "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
        "denseScore": 0.851176917552948,
        "score": 0.851176917552948
      },
      {
        "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
        "denseScore": 0.8500742316246033,
        "score": 0.8500742316246033
      },
      {
        "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
        "denseScore": 0.8500374555587769,
        "score": 0.8500374555587769
      },
      {
        "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
        "denseScore": 0.8494212627410889,
        "score": 0.8494212627410889
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1310,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-COMMON-001",
        "anchor": "KST",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "originHit": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26"
    },
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "originHit": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805"
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "originHit": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004"
    },
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "originHit": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1"
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "originHit": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380"
    }
  ]
}
```

## Q015

요일마다 도시락 인원수를 몇 명까지 설정할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-006",
      "anchor": "1명부터 6명까지",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 409,
          "quote": "- 정책 내용: 고객은 선택한 각 배송 요일의 인원수를 1명부터 6명까지 서로 다르게 설정할 수 있다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q015",
  "group": "G008",
  "question": "요일마다 도시락 인원수를 몇 명까지 설정할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.107299998911913,
  "retrievalMs": 2.737900000283844,
  "hits": [
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "denseScore": 0.9335622787475586,
      "score": 0.9335622787475586
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8863852024078369,
      "score": 0.8863852024078369
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "denseScore": 0.8794600963592529,
      "score": 0.8794600963592529
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8792938590049744,
      "score": 0.8792938590049744
    },
    {
      "chunkId": "knowledge-3-78f67e3b853f76613e994c478152d7501c8b2c68fb8392cd9ad7b9bdea24a980",
      "denseScore": 0.8780339956283569,
      "score": 0.8780339956283569
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "denseScore": 0.9335622787475586,
      "score": 0.9335622787475586
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8863852024078369,
      "score": 0.8863852024078369
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "denseScore": 0.8794600963592529,
      "score": 0.8794600963592529
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8792938590049744,
      "score": 0.8792938590049744
    },
    {
      "chunkId": "knowledge-3-78f67e3b853f76613e994c478152d7501c8b2c68fb8392cd9ad7b9bdea24a980",
      "denseScore": 0.8780339956283569,
      "score": 0.8780339956283569
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
        "denseScore": 0.9335622787475586,
        "score": 0.9335622787475586
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8863852024078369,
        "score": 0.8863852024078369
      },
      {
        "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
        "denseScore": 0.8794600963592529,
        "score": 0.8794600963592529
      },
      {
        "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
        "denseScore": 0.8792938590049744,
        "score": 0.8792938590049744
      },
      {
        "chunkId": "knowledge-3-78f67e3b853f76613e994c478152d7501c8b2c68fb8392cd9ad7b9bdea24a980",
        "denseScore": 0.8780339956283569,
        "score": 0.8780339956283569
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 914,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-006",
        "anchor": "1명부터 6명까지",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 5,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "originHit": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "originHit": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab"
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "originHit": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23"
    },
    {
      "chunkId": "knowledge-3-78f67e3b853f76613e994c478152d7501c8b2c68fb8392cd9ad7b9bdea24a980",
      "originHit": "knowledge-3-78f67e3b853f76613e994c478152d7501c8b2c68fb8392cd9ad7b9bdea24a980"
    }
  ]
}
```

## Q016

배송 요일별 인원수의 허용 범위를 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-006",
      "anchor": "1명부터 6명까지",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 409,
          "quote": "- 정책 내용: 고객은 선택한 각 배송 요일의 인원수를 1명부터 6명까지 서로 다르게 설정할 수 있다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q016",
  "group": "G008",
  "question": "배송 요일별 인원수의 허용 범위를 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.158000000956235,
  "retrievalMs": 2.8241999989404576,
  "hits": [
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.891264796257019,
      "score": 0.891264796257019
    },
    {
      "chunkId": "knowledge-1-8437ad0f32d0707506b1b142defd4aa977a663dbe6869b4323cfcc5647fb621c",
      "denseScore": 0.8847936987876892,
      "score": 0.8847936987876892
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8803848624229431,
      "score": 0.8803848624229431
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8765351176261902,
      "score": 0.8765351176261902
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "denseScore": 0.8740620613098145,
      "score": 0.8740620613098145
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.891264796257019,
      "score": 0.891264796257019
    },
    {
      "chunkId": "knowledge-1-8437ad0f32d0707506b1b142defd4aa977a663dbe6869b4323cfcc5647fb621c",
      "denseScore": 0.8847936987876892,
      "score": 0.8847936987876892
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8803848624229431,
      "score": 0.8803848624229431
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8765351176261902,
      "score": 0.8765351176261902
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "denseScore": 0.8740620613098145,
      "score": 0.8740620613098145
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
        "denseScore": 0.891264796257019,
        "score": 0.891264796257019
      },
      {
        "chunkId": "knowledge-1-8437ad0f32d0707506b1b142defd4aa977a663dbe6869b4323cfcc5647fb621c",
        "denseScore": 0.8847936987876892,
        "score": 0.8847936987876892
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8803848624229431,
        "score": 0.8803848624229431
      },
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.8765351176261902,
        "score": 0.8765351176261902
      },
      {
        "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
        "denseScore": 0.8740620613098145,
        "score": 0.8740620613098145
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 708,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-006",
        "anchor": "1명부터 6명까지",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "originHit": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238"
    },
    {
      "chunkId": "knowledge-1-8437ad0f32d0707506b1b142defd4aa977a663dbe6869b4323cfcc5647fb621c",
      "originHit": "knowledge-1-8437ad0f32d0707506b1b142defd4aa977a663dbe6869b4323cfcc5647fb621c"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "originHit": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab"
    }
  ]
}
```

## Q017

첫 이용 기간은 언제부터 시작하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-007",
      "anchor": "가장 빠른 실제 배송일",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 419,
          "quote": "- 정책 내용: 첫 이용 기간 시작일은 구독 신청의 처리 기준 시각으로 계산한 반영 기준일 이후 가능한 가장 빠른 실제 배송일로 정하고, 첫 결제 성공 시 시작 예정 상태로 확정한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 424,
          "quote": "- 반영 기준일부터 고객이 선택한 배송 요일을 확인하고, 일요일과 공휴일을 제외한 가장 빠른 실제 배송일을 찾는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 429,
          "quote": "- 가능한 가장 빠른 실제 배송일의 `00:00 KST`에 구독 상태를 `시작 예정`에서 `이용 중`으로 바꾸고 첫 28일 이용 기간을 시작한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 435,
          "quote": "- 배송 요일이 월요일·화요일·수요일인 고객의 신청을 2026년 8월 15일 토요일 13:00에 접수하면 다음 날 일요일을 월요일로 조정하여 반영 기준일은 8월 17일 월요일이다. 8월 17일은 대체공휴일이므로 가능한 가장 빠른 실제 배송일인 8월 18일 화요일을 첫 이용 기간 시작일로 미리 계산한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q017",
  "group": "G009",
  "question": "첫 이용 기간은 언제부터 시작하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 8.396700000957935,
  "retrievalMs": 2.2047000002203276,
  "hits": [
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "denseScore": 0.8822347521781921,
      "score": 0.8822347521781921
    },
    {
      "chunkId": "knowledge-1-0ae06507251a1ef57260940c30150022786c2ccca2baa9ca84fb8eff9720084d",
      "denseScore": 0.8810815811157227,
      "score": 0.8810815811157227
    },
    {
      "chunkId": "knowledge-2-9bf413076af4a26902e914d6e8eb0554317981350ee997b983ab719c587dcf9f",
      "denseScore": 0.8798800110816956,
      "score": 0.8798800110816956
    },
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "denseScore": 0.8792258501052856,
      "score": 0.8792258501052856
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8643695116043091,
      "score": 0.8643695116043091
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "denseScore": 0.8822347521781921,
      "score": 0.8822347521781921
    },
    {
      "chunkId": "knowledge-1-0ae06507251a1ef57260940c30150022786c2ccca2baa9ca84fb8eff9720084d",
      "denseScore": 0.8810815811157227,
      "score": 0.8810815811157227
    },
    {
      "chunkId": "knowledge-2-9bf413076af4a26902e914d6e8eb0554317981350ee997b983ab719c587dcf9f",
      "denseScore": 0.8798800110816956,
      "score": 0.8798800110816956
    },
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "denseScore": 0.8792258501052856,
      "score": 0.8792258501052856
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8643695116043091,
      "score": 0.8643695116043091
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
        "denseScore": 0.8822347521781921,
        "score": 0.8822347521781921
      },
      {
        "chunkId": "knowledge-1-0ae06507251a1ef57260940c30150022786c2ccca2baa9ca84fb8eff9720084d",
        "denseScore": 0.8810815811157227,
        "score": 0.8810815811157227
      },
      {
        "chunkId": "knowledge-2-9bf413076af4a26902e914d6e8eb0554317981350ee997b983ab719c587dcf9f",
        "denseScore": 0.8798800110816956,
        "score": 0.8798800110816956
      },
      {
        "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
        "denseScore": 0.8792258501052856,
        "score": 0.8792258501052856
      },
      {
        "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
        "denseScore": 0.8643695116043091,
        "score": 0.8643695116043091
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 321,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-007",
        "anchor": "가장 빠른 실제 배송일",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "originHit": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f"
    },
    {
      "chunkId": "knowledge-1-0ae06507251a1ef57260940c30150022786c2ccca2baa9ca84fb8eff9720084d",
      "originHit": "knowledge-1-0ae06507251a1ef57260940c30150022786c2ccca2baa9ca84fb8eff9720084d"
    },
    {
      "chunkId": "knowledge-2-9bf413076af4a26902e914d6e8eb0554317981350ee997b983ab719c587dcf9f",
      "originHit": "knowledge-2-9bf413076af4a26902e914d6e8eb0554317981350ee997b983ab719c587dcf9f"
    },
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "originHit": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8"
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "originHit": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb"
    }
  ]
}
```

## Q018

신청 후 첫 구독 시작 날짜를 정하는 기준은 무엇인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-007",
      "anchor": "가장 빠른 실제 배송일",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 419,
          "quote": "- 정책 내용: 첫 이용 기간 시작일은 구독 신청의 처리 기준 시각으로 계산한 반영 기준일 이후 가능한 가장 빠른 실제 배송일로 정하고, 첫 결제 성공 시 시작 예정 상태로 확정한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 424,
          "quote": "- 반영 기준일부터 고객이 선택한 배송 요일을 확인하고, 일요일과 공휴일을 제외한 가장 빠른 실제 배송일을 찾는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 429,
          "quote": "- 가능한 가장 빠른 실제 배송일의 `00:00 KST`에 구독 상태를 `시작 예정`에서 `이용 중`으로 바꾸고 첫 28일 이용 기간을 시작한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 435,
          "quote": "- 배송 요일이 월요일·화요일·수요일인 고객의 신청을 2026년 8월 15일 토요일 13:00에 접수하면 다음 날 일요일을 월요일로 조정하여 반영 기준일은 8월 17일 월요일이다. 8월 17일은 대체공휴일이므로 가능한 가장 빠른 실제 배송일인 8월 18일 화요일을 첫 이용 기간 시작일로 미리 계산한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q018",
  "group": "G009",
  "question": "신청 후 첫 구독 시작 날짜를 정하는 기준은 무엇인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.174699999173754,
  "retrievalMs": 2.7021000005333917,
  "hits": [
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "denseScore": 0.9147661924362183,
      "score": 0.9147661924362183
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.897963285446167,
      "score": 0.897963285446167
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.8946258425712585,
      "score": 0.8946258425712585
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "denseScore": 0.8930984735488892,
      "score": 0.8930984735488892
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8888067007064819,
      "score": 0.8888067007064819
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "denseScore": 0.9147661924362183,
      "score": 0.9147661924362183
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.897963285446167,
      "score": 0.897963285446167
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.8946258425712585,
      "score": 0.8946258425712585
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "denseScore": 0.8930984735488892,
      "score": 0.8930984735488892
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8888067007064819,
      "score": 0.8888067007064819
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
        "denseScore": 0.9147661924362183,
        "score": 0.9147661924362183
      },
      {
        "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
        "denseScore": 0.897963285446167,
        "score": 0.897963285446167
      },
      {
        "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
        "denseScore": 0.8946258425712585,
        "score": 0.8946258425712585
      },
      {
        "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
        "denseScore": 0.8930984735488892,
        "score": 0.8930984735488892
      },
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8888067007064819,
        "score": 0.8888067007064819
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 990,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-007",
        "anchor": "가장 빠른 실제 배송일",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "originHit": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8"
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "originHit": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd"
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "originHit": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26"
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "originHit": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233"
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    }
  ]
}
```

## Q023

선택한 배송 요일은 매주 반복되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-010",
      "anchor": "매주 동일하게",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 472,
          "quote": "- 정책 내용: 고객이 선택한 1개부터 6개의 배송 요일은 28일 이용 기간 동안 매주 동일하게 반복 적용한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q023",
  "group": "G012",
  "question": "선택한 배송 요일은 매주 반복되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.54560000031779,
  "retrievalMs": 2.0188000016787555,
  "hits": [
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8988026976585388,
      "score": 0.8988026976585388
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8855670094490051,
      "score": 0.8855670094490051
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "denseScore": 0.8841572999954224,
      "score": 0.8841572999954224
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8834565877914429,
      "score": 0.8834565877914429
    },
    {
      "chunkId": "knowledge-1-6cb437889db3458c0f62ff4bc7ae551f6db11a3161698e22998e4680d1c769ff",
      "denseScore": 0.8823387026786804,
      "score": 0.8823387026786804
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8988026976585388,
      "score": 0.8988026976585388
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8855670094490051,
      "score": 0.8855670094490051
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "denseScore": 0.8841572999954224,
      "score": 0.8841572999954224
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8834565877914429,
      "score": 0.8834565877914429
    },
    {
      "chunkId": "knowledge-1-6cb437889db3458c0f62ff4bc7ae551f6db11a3161698e22998e4680d1c769ff",
      "denseScore": 0.8823387026786804,
      "score": 0.8823387026786804
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
        "denseScore": 0.8988026976585388,
        "score": 0.8988026976585388
      },
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.8855670094490051,
        "score": 0.8855670094490051
      },
      {
        "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
        "denseScore": 0.8841572999954224,
        "score": 0.8841572999954224
      },
      {
        "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
        "denseScore": 0.8834565877914429,
        "score": 0.8834565877914429
      },
      {
        "chunkId": "knowledge-1-6cb437889db3458c0f62ff4bc7ae551f6db11a3161698e22998e4680d1c769ff",
        "denseScore": 0.8823387026786804,
        "score": 0.8823387026786804
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 293,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-010",
        "anchor": "매주 동일하게",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "originHit": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80"
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "originHit": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6"
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "originHit": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94"
    },
    {
      "chunkId": "knowledge-1-6cb437889db3458c0f62ff4bc7ae551f6db11a3161698e22998e4680d1c769ff",
      "originHit": "knowledge-1-6cb437889db3458c0f62ff4bc7ae551f6db11a3161698e22998e4680d1c769ff"
    }
  ]
}
```

## Q024

구독 기간 동안 요일 설정이 주마다 유지되는지 알고 싶어요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-010",
      "anchor": "매주 동일하게",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 472,
          "quote": "- 정책 내용: 고객이 선택한 1개부터 6개의 배송 요일은 28일 이용 기간 동안 매주 동일하게 반복 적용한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q024",
  "group": "G012",
  "question": "구독 기간 동안 요일 설정이 주마다 유지되는지 알고 싶어요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.491299999761395,
  "retrievalMs": 2.2028999992471654,
  "hits": [
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.9031651020050049,
      "score": 0.9031651020050049
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.89253830909729,
      "score": 0.89253830909729
    },
    {
      "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
      "denseScore": 0.8920263051986694,
      "score": 0.8920263051986694
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "denseScore": 0.8911641836166382,
      "score": 0.8911641836166382
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.8910035490989685,
      "score": 0.8910035490989685
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.9031651020050049,
      "score": 0.9031651020050049
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.89253830909729,
      "score": 0.89253830909729
    },
    {
      "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
      "denseScore": 0.8920263051986694,
      "score": 0.8920263051986694
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "denseScore": 0.8911641836166382,
      "score": 0.8911641836166382
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.8910035490989685,
      "score": 0.8910035490989685
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
        "denseScore": 0.9031651020050049,
        "score": 0.9031651020050049
      },
      {
        "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
        "denseScore": 0.89253830909729,
        "score": 0.89253830909729
      },
      {
        "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
        "denseScore": 0.8920263051986694,
        "score": 0.8920263051986694
      },
      {
        "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
        "denseScore": 0.8911641836166382,
        "score": 0.8911641836166382
      },
      {
        "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
        "denseScore": 0.8910035490989685,
        "score": 0.8910035490989685
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 786,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-010",
        "anchor": "매주 동일하게",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "originHit": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94"
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "originHit": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238"
    },
    {
      "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
      "originHit": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd"
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "originHit": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233"
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "originHit": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26"
    }
  ]
}
```

## Q025

배송받을 시간대는 무엇이 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-011",
      "anchor": "11:00~13:00",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 493,
          "quote": "- 정책 내용: 고객은 선택한 배송 요일마다 `11:00~13:00` 또는 `17:00~19:00` 중 하나의 배송 시간대를 선택한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q025",
  "group": "G013",
  "question": "배송받을 시간대는 무엇이 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.405799999512965,
  "retrievalMs": 2.3467999999411404,
  "hits": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8822085857391357,
      "score": 0.8822085857391357
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "denseScore": 0.8790527582168579,
      "score": 0.8790527582168579
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "denseScore": 0.8722818493843079,
      "score": 0.8722818493843079
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8688544631004333,
      "score": 0.8688544631004333
    },
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "denseScore": 0.8676605820655823,
      "score": 0.8676605820655823
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8822085857391357,
      "score": 0.8822085857391357
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "denseScore": 0.8790527582168579,
      "score": 0.8790527582168579
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "denseScore": 0.8722818493843079,
      "score": 0.8722818493843079
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8688544631004333,
      "score": 0.8688544631004333
    },
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "denseScore": 0.8676605820655823,
      "score": 0.8676605820655823
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
        "denseScore": 0.8822085857391357,
        "score": 0.8822085857391357
      },
      {
        "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
        "denseScore": 0.8790527582168579,
        "score": 0.8790527582168579
      },
      {
        "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
        "denseScore": 0.8722818493843079,
        "score": 0.8722818493843079
      },
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.8688544631004333,
        "score": 0.8688544631004333
      },
      {
        "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
        "denseScore": 0.8676605820655823,
        "score": 0.8676605820655823
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 705,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-011",
        "anchor": "11:00~13:00",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "originHit": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb"
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "originHit": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6"
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "originHit": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4"
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "originHit": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5"
    }
  ]
}
```

## Q026

요일별로 고를 수 있는 배송 시간 구간을 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-011",
      "anchor": "11:00~13:00",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 493,
          "quote": "- 정책 내용: 고객은 선택한 배송 요일마다 `11:00~13:00` 또는 `17:00~19:00` 중 하나의 배송 시간대를 선택한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q026",
  "group": "G013",
  "question": "요일별로 고를 수 있는 배송 시간 구간을 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.901299999910407,
  "retrievalMs": 2.648300000146264,
  "hits": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8807994723320007,
      "score": 0.8807994723320007
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8773806691169739,
      "score": 0.8773806691169739
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8739163875579834,
      "score": 0.8739163875579834
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8692182302474976,
      "score": 0.8692182302474976
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "denseScore": 0.8687810897827148,
      "score": 0.8687810897827148
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8807994723320007,
      "score": 0.8807994723320007
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8773806691169739,
      "score": 0.8773806691169739
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8739163875579834,
      "score": 0.8739163875579834
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8692182302474976,
      "score": 0.8692182302474976
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "denseScore": 0.8687810897827148,
      "score": 0.8687810897827148
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
        "denseScore": 0.8807994723320007,
        "score": 0.8807994723320007
      },
      {
        "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
        "denseScore": 0.8773806691169739,
        "score": 0.8773806691169739
      },
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.8739163875579834,
        "score": 0.8739163875579834
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8692182302474976,
        "score": 0.8692182302474976
      },
      {
        "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
        "denseScore": 0.8687810897827148,
        "score": 0.8687810897827148
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 823,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-011",
        "anchor": "11:00~13:00",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "originHit": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb"
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "originHit": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80"
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4",
      "originHit": "knowledge-1-be7d2c4c08de1e5ee5addc721716c7981bfcf84b41a9b2ba9bb12ee8db1d71e4"
    }
  ]
}
```

## Q027

요일마다 배송지와 인원수를 다르게 지정할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-012",
      "anchor": "각각 설정",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 501,
          "quote": "- 정책 내용: 고객은 선택한 배송 요일마다 1명부터 6명까지의 인원수, 배송지 하나, 배송 시간대 하나를 각각 설정한다. 서로 다른 배송 요일에 인원수·배송지·시간대를 같게 설정하거나 각각 다르게 설정할 수 있다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q027",
  "group": "G014",
  "question": "요일마다 배송지와 인원수를 다르게 지정할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.224500000025728,
  "retrievalMs": 2.357399998800247,
  "hits": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.888379693031311,
      "score": 0.888379693031311
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.8857099413871765,
      "score": 0.8857099413871765
    },
    {
      "chunkId": "knowledge-2-772a44fbfb8b3a69c227d5e8a9b8ab37319169e7c782cc8e96a26e8715849cba",
      "denseScore": 0.8773031234741211,
      "score": 0.8773031234741211
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8754836916923523,
      "score": 0.8754836916923523
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8748601675033569,
      "score": 0.8748601675033569
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.888379693031311,
      "score": 0.888379693031311
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.8857099413871765,
      "score": 0.8857099413871765
    },
    {
      "chunkId": "knowledge-2-772a44fbfb8b3a69c227d5e8a9b8ab37319169e7c782cc8e96a26e8715849cba",
      "denseScore": 0.8773031234741211,
      "score": 0.8773031234741211
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8754836916923523,
      "score": 0.8754836916923523
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8748601675033569,
      "score": 0.8748601675033569
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.888379693031311,
        "score": 0.888379693031311
      },
      {
        "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
        "denseScore": 0.8857099413871765,
        "score": 0.8857099413871765
      },
      {
        "chunkId": "knowledge-2-772a44fbfb8b3a69c227d5e8a9b8ab37319169e7c782cc8e96a26e8715849cba",
        "denseScore": 0.8773031234741211,
        "score": 0.8773031234741211
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8754836916923523,
        "score": 0.8754836916923523
      },
      {
        "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
        "denseScore": 0.8748601675033569,
        "score": 0.8748601675033569
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 747,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-012",
        "anchor": "각각 설정",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "originHit": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238"
    },
    {
      "chunkId": "knowledge-2-772a44fbfb8b3a69c227d5e8a9b8ab37319169e7c782cc8e96a26e8715849cba",
      "originHit": "knowledge-2-772a44fbfb8b3a69c227d5e8a9b8ab37319169e7c782cc8e96a26e8715849cba"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "originHit": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94"
    }
  ]
}
```

## Q028

월요일과 금요일의 주소나 시간대를 따로 설정해도 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-012",
      "anchor": "각각 설정",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 501,
          "quote": "- 정책 내용: 고객은 선택한 배송 요일마다 1명부터 6명까지의 인원수, 배송지 하나, 배송 시간대 하나를 각각 설정한다. 서로 다른 배송 요일에 인원수·배송지·시간대를 같게 설정하거나 각각 다르게 설정할 수 있다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q028",
  "group": "G014",
  "question": "월요일과 금요일의 주소나 시간대를 따로 설정해도 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.621300000115298,
  "retrievalMs": 1.7939000008482253,
  "hits": [
    {
      "chunkId": "knowledge-1-8287c92b7f8aa8544c8a645ca1c545a665873fb80cd463feb3196fe38b3c28da",
      "denseScore": 0.8878952264785767,
      "score": 0.8878952264785767
    },
    {
      "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
      "denseScore": 0.882240891456604,
      "score": 0.882240891456604
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "denseScore": 0.8818082213401794,
      "score": 0.8818082213401794
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8772239685058594,
      "score": 0.8772239685058594
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8708351254463196,
      "score": 0.8708351254463196
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-8287c92b7f8aa8544c8a645ca1c545a665873fb80cd463feb3196fe38b3c28da",
      "denseScore": 0.8878952264785767,
      "score": 0.8878952264785767
    },
    {
      "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
      "denseScore": 0.882240891456604,
      "score": 0.882240891456604
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "denseScore": 0.8818082213401794,
      "score": 0.8818082213401794
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8772239685058594,
      "score": 0.8772239685058594
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8708351254463196,
      "score": 0.8708351254463196
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-8287c92b7f8aa8544c8a645ca1c545a665873fb80cd463feb3196fe38b3c28da",
        "denseScore": 0.8878952264785767,
        "score": 0.8878952264785767
      },
      {
        "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
        "denseScore": 0.882240891456604,
        "score": 0.882240891456604
      },
      {
        "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
        "denseScore": 0.8818082213401794,
        "score": 0.8818082213401794
      },
      {
        "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
        "denseScore": 0.8772239685058594,
        "score": 0.8772239685058594
      },
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.8708351254463196,
        "score": 0.8708351254463196
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 221,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-012",
        "anchor": "각각 설정",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 5,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-8287c92b7f8aa8544c8a645ca1c545a665873fb80cd463feb3196fe38b3c28da",
      "originHit": "knowledge-1-8287c92b7f8aa8544c8a645ca1c545a665873fb80cd463feb3196fe38b3c28da"
    },
    {
      "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
      "originHit": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a"
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "originHit": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637"
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "originHit": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80"
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    }
  ]
}
```

## Q031

한 계정에서 구독을 몇 개 유지할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-014",
      "anchor": "고객당 하나",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 559,
          "quote": "- 정책 내용: 인증 서비스가 제공한 같은 고객 식별자를 기준으로 구독 관계는 고객당 하나만 유지한다. 첫 결제 실패·시작 취소·종료 후 다시 구독하더라도 기존 구독을 재사용하고, 현재 상태와 구독 상태 이력으로 전체 생명주기를 관리한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q031",
  "group": "G016",
  "question": "한 계정에서 구독을 몇 개 유지할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.276999999608961,
  "retrievalMs": 2.8640000000450527,
  "hits": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8701779246330261,
      "score": 0.8701779246330261
    },
    {
      "chunkId": "knowledge-1-f89e90bfb18dcf407ac680644a484865f682cad981a615bb9055eecb4437bff6",
      "denseScore": 0.8700935244560242,
      "score": 0.8700935244560242
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8683785200119019,
      "score": 0.8683785200119019
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8682093620300293,
      "score": 0.8682093620300293
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8646048307418823,
      "score": 0.8646048307418823
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8701779246330261,
      "score": 0.8701779246330261
    },
    {
      "chunkId": "knowledge-1-f89e90bfb18dcf407ac680644a484865f682cad981a615bb9055eecb4437bff6",
      "denseScore": 0.8700935244560242,
      "score": 0.8700935244560242
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8683785200119019,
      "score": 0.8683785200119019
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8682093620300293,
      "score": 0.8682093620300293
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8646048307418823,
      "score": 0.8646048307418823
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8701779246330261,
        "score": 0.8701779246330261
      },
      {
        "chunkId": "knowledge-1-f89e90bfb18dcf407ac680644a484865f682cad981a615bb9055eecb4437bff6",
        "denseScore": 0.8700935244560242,
        "score": 0.8700935244560242
      },
      {
        "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
        "denseScore": 0.8683785200119019,
        "score": 0.8683785200119019
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8682093620300293,
        "score": 0.8682093620300293
      },
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.8646048307418823,
        "score": 0.8646048307418823
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1028,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-014",
        "anchor": "고객당 하나",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-1-f89e90bfb18dcf407ac680644a484865f682cad981a615bb9055eecb4437bff6",
      "originHit": "knowledge-1-f89e90bfb18dcf407ac680644a484865f682cad981a615bb9055eecb4437bff6"
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "originHit": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    }
  ]
}
```

## Q032

고객 한 명이 여러 구독을 동시에 만들 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-014",
      "anchor": "고객당 하나",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 559,
          "quote": "- 정책 내용: 인증 서비스가 제공한 같은 고객 식별자를 기준으로 구독 관계는 고객당 하나만 유지한다. 첫 결제 실패·시작 취소·종료 후 다시 구독하더라도 기존 구독을 재사용하고, 현재 상태와 구독 상태 이력으로 전체 생명주기를 관리한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q032",
  "group": "G016",
  "question": "고객 한 명이 여러 구독을 동시에 만들 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.844300000826479,
  "retrievalMs": 2.738099999987753,
  "hits": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8722343444824219,
      "score": 0.8722343444824219
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8669137954711914,
      "score": 0.8669137954711914
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.8661646246910095,
      "score": 0.8661646246910095
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8643364906311035,
      "score": 0.8643364906311035
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8633332252502441,
      "score": 0.8633332252502441
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8722343444824219,
      "score": 0.8722343444824219
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8669137954711914,
      "score": 0.8669137954711914
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "denseScore": 0.8661646246910095,
      "score": 0.8661646246910095
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8643364906311035,
      "score": 0.8643364906311035
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8633332252502441,
      "score": 0.8633332252502441
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
        "denseScore": 0.8722343444824219,
        "score": 0.8722343444824219
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8669137954711914,
        "score": 0.8669137954711914
      },
      {
        "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
        "denseScore": 0.8661646246910095,
        "score": 0.8661646246910095
      },
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8643364906311035,
        "score": 0.8643364906311035
      },
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.8633332252502441,
        "score": 0.8633332252502441
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1024,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-014",
        "anchor": "고객당 하나",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "originHit": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238",
      "originHit": "knowledge-1-37f1d31c7ee6b1997ce59f211e6ae6ed2c9d6370d39b9eca12948931838a4238"
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    }
  ]
}
```

## Q033

구독 해지와 회원 탈퇴는 같은 처리인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-015",
      "anchor": "구독 해지는 구독 서비스",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 589,
          "quote": "- 정책 내용: 구독 해지는 구독 서비스가 처리하고, 회원 탈퇴는 인증 서비스가 처리한다. 인증 서비스는 구독 해지·환불을 대신 실행하거나, 회원 탈퇴 과정에서 구독 상태를 강제로 바꾸지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q033",
  "group": "G017",
  "question": "구독 해지와 회원 탈퇴는 같은 처리인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.44329999947513,
  "retrievalMs": 2.412400001048809,
  "hits": [
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.9008028507232666,
      "score": 0.9008028507232666
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.9002474546432495,
      "score": 0.9002474546432495
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8766500353813171,
      "score": 0.8766500353813171
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8748384118080139,
      "score": 0.8748384118080139
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.873880922794342,
      "score": 0.873880922794342
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.9008028507232666,
      "score": 0.9008028507232666
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.9002474546432495,
      "score": 0.9002474546432495
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8766500353813171,
      "score": 0.8766500353813171
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8748384118080139,
      "score": 0.8748384118080139
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.873880922794342,
      "score": 0.873880922794342
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
        "denseScore": 0.9008028507232666,
        "score": 0.9008028507232666
      },
      {
        "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
        "denseScore": 0.9002474546432495,
        "score": 0.9002474546432495
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8766500353813171,
        "score": 0.8766500353813171
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8748384118080139,
        "score": 0.8748384118080139
      },
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.873880922794342,
        "score": 0.873880922794342
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 882,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-015",
        "anchor": "구독 해지는 구독 서비스",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "originHit": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba"
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "originHit": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    }
  ]
}
```

## Q034

계정 탈퇴와 구독 종료의 차이를 설명해 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-015",
      "anchor": "구독 해지는 구독 서비스",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 589,
          "quote": "- 정책 내용: 구독 해지는 구독 서비스가 처리하고, 회원 탈퇴는 인증 서비스가 처리한다. 인증 서비스는 구독 해지·환불을 대신 실행하거나, 회원 탈퇴 과정에서 구독 상태를 강제로 바꾸지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q034",
  "group": "G017",
  "question": "계정 탈퇴와 구독 종료의 차이를 설명해 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.688000000096508,
  "retrievalMs": 2.513600000384031,
  "hits": [
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.8848147988319397,
      "score": 0.8848147988319397
    },
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.8842760324478149,
      "score": 0.8842760324478149
    },
    {
      "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
      "denseScore": 0.8823713064193726,
      "score": 0.8823713064193726
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8745999336242676,
      "score": 0.8745999336242676
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8743107318878174,
      "score": 0.8743107318878174
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.8848147988319397,
      "score": 0.8848147988319397
    },
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.8842760324478149,
      "score": 0.8842760324478149
    },
    {
      "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
      "denseScore": 0.8823713064193726,
      "score": 0.8823713064193726
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8745999336242676,
      "score": 0.8745999336242676
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8743107318878174,
      "score": 0.8743107318878174
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
        "denseScore": 0.8848147988319397,
        "score": 0.8848147988319397
      },
      {
        "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
        "denseScore": 0.8842760324478149,
        "score": 0.8842760324478149
      },
      {
        "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
        "denseScore": 0.8823713064193726,
        "score": 0.8823713064193726
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8745999336242676,
        "score": 0.8745999336242676
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8743107318878174,
        "score": 0.8743107318878174
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 765,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-015",
        "anchor": "구독 해지는 구독 서비스",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "originHit": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120"
    },
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "originHit": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba"
    },
    {
      "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
      "originHit": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    }
  ]
}
```

## Q045

정기결제 재시도까지 실패하면 어떻게 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-006",
      "anchor": "다음 이용 기간을 시작하지 않는다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 728,
          "quote": "- 다음 이용 기간을 시작하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q045",
  "group": "G023",
  "question": "정기결제 재시도까지 실패하면 어떻게 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.630500000639586,
  "retrievalMs": 2.72180000138178,
  "hits": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "denseScore": 0.9047501683235168,
      "score": 0.9047501683235168
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8872135281562805,
      "score": 0.8872135281562805
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "denseScore": 0.8862794637680054,
      "score": 0.8862794637680054
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.8798550367355347,
      "score": 0.8798550367355347
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8792579174041748,
      "score": 0.8792579174041748
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "denseScore": 0.9047501683235168,
      "score": 0.9047501683235168
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8872135281562805,
      "score": 0.8872135281562805
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "denseScore": 0.8862794637680054,
      "score": 0.8862794637680054
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.8798550367355347,
      "score": 0.8798550367355347
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8792579174041748,
      "score": 0.8792579174041748
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
        "denseScore": 0.9047501683235168,
        "score": 0.9047501683235168
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8872135281562805,
        "score": 0.8872135281562805
      },
      {
        "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
        "denseScore": 0.8862794637680054,
        "score": 0.8862794637680054
      },
      {
        "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
        "denseScore": 0.8798550367355347,
        "score": 0.8798550367355347
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8792579174041748,
        "score": 0.8792579174041748
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1171,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-006",
        "anchor": "다음 이용 기간을 시작하지 않는다",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 5,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "originHit": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "originHit": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004"
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "originHit": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    }
  ]
}
```

## Q046

마지막 자동결제 시도도 실패했을 때 구독 처리 원칙을 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-006",
      "anchor": "다음 이용 기간을 시작하지 않는다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 728,
          "quote": "- 다음 이용 기간을 시작하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q046",
  "group": "G023",
  "question": "마지막 자동결제 시도도 실패했을 때 구독 처리 원칙을 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.079899999458576,
  "retrievalMs": 2.940200000011828,
  "hits": [
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.9070727825164795,
      "score": 0.9070727825164795
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.9034746885299683,
      "score": 0.9034746885299683
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.9028241634368896,
      "score": 0.9028241634368896
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.9025835990905762,
      "score": 0.9025835990905762
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.899949312210083,
      "score": 0.899949312210083
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.9070727825164795,
      "score": 0.9070727825164795
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.9034746885299683,
      "score": 0.9034746885299683
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.9028241634368896,
      "score": 0.9028241634368896
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.9025835990905762,
      "score": 0.9025835990905762
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.899949312210083,
      "score": 0.899949312210083
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.9070727825164795,
        "score": 0.9070727825164795
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.9034746885299683,
        "score": 0.9034746885299683
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.9028241634368896,
        "score": 0.9028241634368896
      },
      {
        "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
        "denseScore": 0.9025835990905762,
        "score": 0.9025835990905762
      },
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.899949312210083,
        "score": 0.899949312210083
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1295,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-006",
        "anchor": "다음 이용 기간을 시작하지 않는다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "originHit": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7"
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    }
  ]
}
```

## Q053

자동결제 카드를 여러 장 등록할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-011",
      "anchor": "여러 개 등록",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 863,
          "quote": "- 정책 내용: 고객은 검증된 자동결제수단을 여러 개 등록할 수 있다. 사용 가능한 자동결제수단이 하나도 없는 상태에서 첫 수단의 등록·검증에 성공하면 해당 수단을 현재 결제수단으로 자동 지정한다. 이미 사용 가능한 자동결제수단이 하나 이상 있으면 새 수단 등록만으로 기존 현재 결제수단을 변경하지 않으며, 고객은 등록·검증된 수단 중 하나를 현재 결제수단으로 선택할 수 있다. 진행 중 구독에는 현재 결제수단이 정확히 하나 있어야 한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q053",
  "group": "G027",
  "question": "자동결제 카드를 여러 장 등록할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.582600000110688,
  "retrievalMs": 2.4948999998741783,
  "hits": [
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "denseScore": 0.8863785266876221,
      "score": 0.8863785266876221
    },
    {
      "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
      "denseScore": 0.8656226992607117,
      "score": 0.8656226992607117
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.8645123243331909,
      "score": 0.8645123243331909
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8636432886123657,
      "score": 0.8636432886123657
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8448160886764526,
      "score": 0.8448160886764526
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "denseScore": 0.8863785266876221,
      "score": 0.8863785266876221
    },
    {
      "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
      "denseScore": 0.8656226992607117,
      "score": 0.8656226992607117
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.8645123243331909,
      "score": 0.8645123243331909
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8636432886123657,
      "score": 0.8636432886123657
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8448160886764526,
      "score": 0.8448160886764526
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
        "denseScore": 0.8863785266876221,
        "score": 0.8863785266876221
      },
      {
        "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
        "denseScore": 0.8656226992607117,
        "score": 0.8656226992607117
      },
      {
        "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
        "denseScore": 0.8645123243331909,
        "score": 0.8645123243331909
      },
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.8636432886123657,
        "score": 0.8636432886123657
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8448160886764526,
        "score": 0.8448160886764526
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 931,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-011",
        "anchor": "여러 개 등록",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 1,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "originHit": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2"
    },
    {
      "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
      "originHit": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be"
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "originHit": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78"
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    }
  ]
}
```

## Q054

사용할 결제수단을 복수로 등록해도 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-011",
      "anchor": "여러 개 등록",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 863,
          "quote": "- 정책 내용: 고객은 검증된 자동결제수단을 여러 개 등록할 수 있다. 사용 가능한 자동결제수단이 하나도 없는 상태에서 첫 수단의 등록·검증에 성공하면 해당 수단을 현재 결제수단으로 자동 지정한다. 이미 사용 가능한 자동결제수단이 하나 이상 있으면 새 수단 등록만으로 기존 현재 결제수단을 변경하지 않으며, 고객은 등록·검증된 수단 중 하나를 현재 결제수단으로 선택할 수 있다. 진행 중 구독에는 현재 결제수단이 정확히 하나 있어야 한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q054",
  "group": "G027",
  "question": "사용할 결제수단을 복수로 등록해도 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.125200000606128,
  "retrievalMs": 2.405999999609776,
  "hits": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.9055560231208801,
      "score": 0.9055560231208801
    },
    {
      "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
      "denseScore": 0.8890240788459778,
      "score": 0.8890240788459778
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.8883559703826904,
      "score": 0.8883559703826904
    },
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "denseScore": 0.8853391408920288,
      "score": 0.8853391408920288
    },
    {
      "chunkId": "knowledge-3-b3b835b30ce614ccf834ac0812b6dea6140e0e14de9781d9cc91cde193c9e740",
      "denseScore": 0.8807463645935059,
      "score": 0.8807463645935059
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.9055560231208801,
      "score": 0.9055560231208801
    },
    {
      "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
      "denseScore": 0.8890240788459778,
      "score": 0.8890240788459778
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.8883559703826904,
      "score": 0.8883559703826904
    },
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "denseScore": 0.8853391408920288,
      "score": 0.8853391408920288
    },
    {
      "chunkId": "knowledge-3-b3b835b30ce614ccf834ac0812b6dea6140e0e14de9781d9cc91cde193c9e740",
      "denseScore": 0.8807463645935059,
      "score": 0.8807463645935059
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.9055560231208801,
        "score": 0.9055560231208801
      },
      {
        "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
        "denseScore": 0.8890240788459778,
        "score": 0.8890240788459778
      },
      {
        "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
        "denseScore": 0.8883559703826904,
        "score": 0.8883559703826904
      },
      {
        "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
        "denseScore": 0.8853391408920288,
        "score": 0.8853391408920288
      },
      {
        "chunkId": "knowledge-3-b3b835b30ce614ccf834ac0812b6dea6140e0e14de9781d9cc91cde193c9e740",
        "denseScore": 0.8807463645935059,
        "score": 0.8807463645935059
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 703,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-011",
        "anchor": "여러 개 등록",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 1,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    },
    {
      "chunkId": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be",
      "originHit": "knowledge-3-9f9574e6b62d9f9c5a36e30952c53ccddb27cd1d924b2a4618acad888b7f71be"
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "originHit": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78"
    },
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "originHit": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2"
    },
    {
      "chunkId": "knowledge-3-b3b835b30ce614ccf834ac0812b6dea6140e0e14de9781d9cc91cde193c9e740",
      "originHit": "knowledge-3-b3b835b30ce614ccf834ac0812b6dea6140e0e14de9781d9cc91cde193c9e740"
    }
  ]
}
```

## Q059

구독 설정 변경 전 날짜의 주문에도 새 설정이 적용되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-002",
      "anchor": "변경 적용일 전",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 962,
          "quote": "- 정책 내용: 구독 설정 변경 적용일 전의 주문은 기존 구독 설정을 유지한다. 변경 적용일부터의 실제 배송일에는 변경된 플랜·배송 요일·배송 요일별 인원수·배송지·배송 시간대를 반영한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q059",
  "group": "G030",
  "question": "구독 설정 변경 전 날짜의 주문에도 새 설정이 적용되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.933100000329432,
  "retrievalMs": 2.0887999999104068,
  "hits": [
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "denseScore": 0.9132551550865173,
      "score": 0.9132551550865173
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.9092600345611572,
      "score": 0.9092600345611572
    },
    {
      "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
      "denseScore": 0.907314658164978,
      "score": 0.907314658164978
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.905105471611023,
      "score": 0.905105471611023
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.9039936661720276,
      "score": 0.9039936661720276
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "denseScore": 0.9132551550865173,
      "score": 0.9132551550865173
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.9092600345611572,
      "score": 0.9092600345611572
    },
    {
      "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
      "denseScore": 0.907314658164978,
      "score": 0.907314658164978
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.905105471611023,
      "score": 0.905105471611023
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.9039936661720276,
      "score": 0.9039936661720276
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
        "denseScore": 0.9132551550865173,
        "score": 0.9132551550865173
      },
      {
        "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
        "denseScore": 0.9092600345611572,
        "score": 0.9092600345611572
      },
      {
        "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
        "denseScore": 0.907314658164978,
        "score": 0.907314658164978
      },
      {
        "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
        "denseScore": 0.905105471611023,
        "score": 0.905105471611023
      },
      {
        "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
        "denseScore": 0.9039936661720276,
        "score": 0.9039936661720276
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 480,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-002",
        "anchor": "변경 적용일 전",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "originHit": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39"
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "originHit": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738"
    },
    {
      "chunkId": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd",
      "originHit": "knowledge-2-569dd94f95a56dd6ab4045c4f42d887d546bf034f77b51948de3a068d7e8d5cd"
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "originHit": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62"
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "originHit": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94"
    }
  ]
}
```

## Q060

설정 변경이 기존 주문에 반영되는 범위가 궁금해요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-002",
      "anchor": "변경 적용일 전",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 962,
          "quote": "- 정책 내용: 구독 설정 변경 적용일 전의 주문은 기존 구독 설정을 유지한다. 변경 적용일부터의 실제 배송일에는 변경된 플랜·배송 요일·배송 요일별 인원수·배송지·배송 시간대를 반영한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q060",
  "group": "G030",
  "question": "설정 변경이 기존 주문에 반영되는 범위가 궁금해요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.432299999592942,
  "retrievalMs": 2.6205000012851087,
  "hits": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.9023104906082153,
      "score": 0.9023104906082153
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.8901183605194092,
      "score": 0.8901183605194092
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8882330656051636,
      "score": 0.8882330656051636
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.8875769972801208,
      "score": 0.8875769972801208
    },
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "denseScore": 0.8854377269744873,
      "score": 0.8854377269744873
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.9023104906082153,
      "score": 0.9023104906082153
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.8901183605194092,
      "score": 0.8901183605194092
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8882330656051636,
      "score": 0.8882330656051636
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.8875769972801208,
      "score": 0.8875769972801208
    },
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "denseScore": 0.8854377269744873,
      "score": 0.8854377269744873
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.9023104906082153,
        "score": 0.9023104906082153
      },
      {
        "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
        "denseScore": 0.8901183605194092,
        "score": 0.8901183605194092
      },
      {
        "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
        "denseScore": 0.8882330656051636,
        "score": 0.8882330656051636
      },
      {
        "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
        "denseScore": 0.8875769972801208,
        "score": 0.8875769972801208
      },
      {
        "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
        "denseScore": 0.8854377269744873,
        "score": 0.8854377269744873
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1066,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-002",
        "anchor": "변경 적용일 전",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "originHit": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738"
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "originHit": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0"
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "originHit": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62"
    },
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "originHit": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39"
    }
  ]
}
```

## Q061

주문에서 사용하는 가격과 주소는 어느 시점의 정보인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-003",
      "anchor": "생성 당시",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 991,
          "quote": "- 정책 내용: 주문에는 생성 당시 적용된 플랜·도시락 단가·해당 배송 요일의 인원수·도시락 금액·배송비·할인금액·실제 배분금액·배송일·배송지·배송 시간대·배달 방식 문자열 코드·`OTHER`의 고객 직접 입력 문자열을 그대로 유지한다. 이후 가격·구독 설정이나 배송지를 변경해도 이미 생성된 주문의 내용은 바뀌지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 995,
          "quote": "8월 10일 주문이 인원수 2명과 배달 방식 `DIRECT`로 생성된 뒤 가격·구독 설정이나 배송지의 배달 방식을 변경해도, 해당 주문은 생성 당시 금액과 내용을 유지한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q061",
  "group": "G031",
  "question": "주문에서 사용하는 가격과 주소는 어느 시점의 정보인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.78380000035395,
  "retrievalMs": 2.441000000544591,
  "hits": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8543738126754761,
      "score": 0.8543738126754761
    },
    {
      "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
      "denseScore": 0.85300612449646,
      "score": 0.85300612449646
    },
    {
      "chunkId": "knowledge-3-dcd75cf3076b56c9439a629f6b25c6460c199c16a28964c28e37e9ecef99c532",
      "denseScore": 0.847061038017273,
      "score": 0.847061038017273
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.8468876481056213,
      "score": 0.8468876481056213
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8459379076957703,
      "score": 0.8459379076957703
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8543738126754761,
      "score": 0.8543738126754761
    },
    {
      "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
      "denseScore": 0.85300612449646,
      "score": 0.85300612449646
    },
    {
      "chunkId": "knowledge-3-dcd75cf3076b56c9439a629f6b25c6460c199c16a28964c28e37e9ecef99c532",
      "denseScore": 0.847061038017273,
      "score": 0.847061038017273
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.8468876481056213,
      "score": 0.8468876481056213
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8459379076957703,
      "score": 0.8459379076957703
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8543738126754761,
        "score": 0.8543738126754761
      },
      {
        "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
        "denseScore": 0.85300612449646,
        "score": 0.85300612449646
      },
      {
        "chunkId": "knowledge-3-dcd75cf3076b56c9439a629f6b25c6460c199c16a28964c28e37e9ecef99c532",
        "denseScore": 0.847061038017273,
        "score": 0.847061038017273
      },
      {
        "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
        "denseScore": 0.8468876481056213,
        "score": 0.8468876481056213
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8459379076957703,
        "score": 0.8459379076957703
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 734,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-003",
        "anchor": "생성 당시",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    },
    {
      "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
      "originHit": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327"
    },
    {
      "chunkId": "knowledge-3-dcd75cf3076b56c9439a629f6b25c6460c199c16a28964c28e37e9ecef99c532",
      "originHit": "knowledge-3-dcd75cf3076b56c9439a629f6b25c6460c199c16a28964c28e37e9ecef99c532"
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "originHit": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    }
  ]
}
```

## Q062

이미 생성된 주문은 어떤 설정값을 보관하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-003",
      "anchor": "생성 당시",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 991,
          "quote": "- 정책 내용: 주문에는 생성 당시 적용된 플랜·도시락 단가·해당 배송 요일의 인원수·도시락 금액·배송비·할인금액·실제 배분금액·배송일·배송지·배송 시간대·배달 방식 문자열 코드·`OTHER`의 고객 직접 입력 문자열을 그대로 유지한다. 이후 가격·구독 설정이나 배송지를 변경해도 이미 생성된 주문의 내용은 바뀌지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 995,
          "quote": "8월 10일 주문이 인원수 2명과 배달 방식 `DIRECT`로 생성된 뒤 가격·구독 설정이나 배송지의 배달 방식을 변경해도, 해당 주문은 생성 당시 금액과 내용을 유지한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q062",
  "group": "G031",
  "question": "이미 생성된 주문은 어떤 설정값을 보관하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.715000000345754,
  "retrievalMs": 3.0120000010356307,
  "hits": [
    {
      "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
      "denseScore": 0.8792750835418701,
      "score": 0.8792750835418701
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8719626069068909,
      "score": 0.8719626069068909
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "denseScore": 0.8666195869445801,
      "score": 0.8666195869445801
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.8665947914123535,
      "score": 0.8665947914123535
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8659810423851013,
      "score": 0.8659810423851013
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
      "denseScore": 0.8792750835418701,
      "score": 0.8792750835418701
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8719626069068909,
      "score": 0.8719626069068909
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "denseScore": 0.8666195869445801,
      "score": 0.8666195869445801
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.8665947914123535,
      "score": 0.8665947914123535
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8659810423851013,
      "score": 0.8659810423851013
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
        "denseScore": 0.8792750835418701,
        "score": 0.8792750835418701
      },
      {
        "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
        "denseScore": 0.8719626069068909,
        "score": 0.8719626069068909
      },
      {
        "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
        "denseScore": 0.8666195869445801,
        "score": 0.8666195869445801
      },
      {
        "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
        "denseScore": 0.8665947914123535,
        "score": 0.8665947914123535
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8659810423851013,
        "score": 0.8659810423851013
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1373,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-003",
        "anchor": "생성 당시",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327",
      "originHit": "knowledge-2-f4c593e86f0b9b9a88a2b6d5a35cc52af2e8b7be0202f41e8a7430a5fa764327"
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "originHit": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0"
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "originHit": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca"
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "originHit": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    }
  ]
}
```

## Q065

주문 한 건의 도시락 수량은 어떻게 정해지나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-005",
      "anchor": "인원수와 같다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1026,
          "quote": "- 정책 내용: 주문 한 건의 도시락 수량은 해당 배송일의 요일에 설정된 인원수와 같다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q065",
  "group": "G033",
  "question": "주문 한 건의 도시락 수량은 어떻게 정해지나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.517400000229827,
  "retrievalMs": 2.2933000000193715,
  "hits": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8925491571426392,
      "score": 0.8925491571426392
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8869390487670898,
      "score": 0.8869390487670898
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "denseScore": 0.8842920064926147,
      "score": 0.8842920064926147
    },
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "denseScore": 0.8830548524856567,
      "score": 0.8830548524856567
    },
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "denseScore": 0.8750240206718445,
      "score": 0.8750240206718445
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8925491571426392,
      "score": 0.8925491571426392
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8869390487670898,
      "score": 0.8869390487670898
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "denseScore": 0.8842920064926147,
      "score": 0.8842920064926147
    },
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "denseScore": 0.8830548524856567,
      "score": 0.8830548524856567
    },
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "denseScore": 0.8750240206718445,
      "score": 0.8750240206718445
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8925491571426392,
        "score": 0.8925491571426392
      },
      {
        "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
        "denseScore": 0.8869390487670898,
        "score": 0.8869390487670898
      },
      {
        "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
        "denseScore": 0.8842920064926147,
        "score": 0.8842920064926147
      },
      {
        "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
        "denseScore": 0.8830548524856567,
        "score": 0.8830548524856567
      },
      {
        "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
        "denseScore": 0.8750240206718445,
        "score": 0.8750240206718445
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 615,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-005",
        "anchor": "인원수와 같다",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "originHit": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23"
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "originHit": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760"
    },
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "originHit": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16"
    },
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "originHit": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932"
    }
  ]
}
```

## Q066

수요일을 3명으로 설정하면 그날 주문에 몇 개가 들어가나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-005",
      "anchor": "인원수와 같다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1026,
          "quote": "- 정책 내용: 주문 한 건의 도시락 수량은 해당 배송일의 요일에 설정된 인원수와 같다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q066",
  "group": "G033",
  "question": "수요일을 3명으로 설정하면 그날 주문에 몇 개가 들어가나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.032300001010299,
  "retrievalMs": 1.8758999995043268,
  "hits": [
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "denseScore": 0.913049578666687,
      "score": 0.913049578666687
    },
    {
      "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
      "denseScore": 0.8942786455154419,
      "score": 0.8942786455154419
    },
    {
      "chunkId": "knowledge-3-e12477c719e277a98f90e82208920137c7db744fb420a5d9d35c485fda251824",
      "denseScore": 0.8924493193626404,
      "score": 0.8924493193626404
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "denseScore": 0.8775729537010193,
      "score": 0.8775729537010193
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.8724480867385864,
      "score": 0.8724480867385864
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "denseScore": 0.913049578666687,
      "score": 0.913049578666687
    },
    {
      "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
      "denseScore": 0.8942786455154419,
      "score": 0.8942786455154419
    },
    {
      "chunkId": "knowledge-3-e12477c719e277a98f90e82208920137c7db744fb420a5d9d35c485fda251824",
      "denseScore": 0.8924493193626404,
      "score": 0.8924493193626404
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "denseScore": 0.8775729537010193,
      "score": 0.8775729537010193
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.8724480867385864,
      "score": 0.8724480867385864
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
        "denseScore": 0.913049578666687,
        "score": 0.913049578666687
      },
      {
        "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
        "denseScore": 0.8942786455154419,
        "score": 0.8942786455154419
      },
      {
        "chunkId": "knowledge-3-e12477c719e277a98f90e82208920137c7db744fb420a5d9d35c485fda251824",
        "denseScore": 0.8924493193626404,
        "score": 0.8924493193626404
      },
      {
        "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
        "denseScore": 0.8775729537010193,
        "score": 0.8775729537010193
      },
      {
        "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
        "denseScore": 0.8724480867385864,
        "score": 0.8724480867385864
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 254,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-005",
        "anchor": "인원수와 같다",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16",
      "originHit": "knowledge-1-f5aa4e470d966a942a9ef94ca1c5629cb560b73b1269bc0d72374bf027ca6a16"
    },
    {
      "chunkId": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a",
      "originHit": "knowledge-1-85e42821823e61c170370f5f2b96862e4f6319800bb098d5303986f98a3fae7a"
    },
    {
      "chunkId": "knowledge-3-e12477c719e277a98f90e82208920137c7db744fb420a5d9d35c485fda251824",
      "originHit": "knowledge-3-e12477c719e277a98f90e82208920137c7db744fb420a5d9d35c485fda251824"
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "originHit": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637"
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "originHit": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12"
    }
  ]
}
```

## Q081

배송 실패한 회차는 다시 배달해 주나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "DLV-POL-ABSENCE-002",
      "anchor": "재배송하지 않고 부분 환불",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 653,
          "quote": "- 배송 실패 회차는 재배송하지 않고 부분 환불한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q081",
  "group": "G041",
  "question": "배송 실패한 회차는 다시 배달해 주나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.270599999988917,
  "retrievalMs": 3.411900001083268,
  "hits": [
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8833598494529724,
      "score": 0.8833598494529724
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8753777146339417,
      "score": 0.8753777146339417
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8743049502372742,
      "score": 0.8743049502372742
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8649615049362183,
      "score": 0.8649615049362183
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8640511631965637,
      "score": 0.8640511631965637
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8833598494529724,
      "score": 0.8833598494529724
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8753777146339417,
      "score": 0.8753777146339417
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8743049502372742,
      "score": 0.8743049502372742
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8649615049362183,
      "score": 0.8649615049362183
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8640511631965637,
      "score": 0.8640511631965637
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
        "denseScore": 0.8833598494529724,
        "score": 0.8833598494529724
      },
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8753777146339417,
        "score": 0.8753777146339417
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8743049502372742,
        "score": 0.8743049502372742
      },
      {
        "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
        "denseScore": 0.8649615049362183,
        "score": 0.8649615049362183
      },
      {
        "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
        "denseScore": 0.8640511631965637,
        "score": 0.8640511631965637
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1767,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "DLV-POL-ABSENCE-002",
        "anchor": "재배송하지 않고 부분 환불",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "originHit": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286"
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "originHit": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38"
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "originHit": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0"
    }
  ]
}
```

## Q082

배달에 실패하면 재배송과 환불 중 어떻게 처리되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "DLV-POL-ABSENCE-002",
      "anchor": "재배송하지 않고 부분 환불",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 653,
          "quote": "- 배송 실패 회차는 재배송하지 않고 부분 환불한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q082",
  "group": "G041",
  "question": "배달에 실패하면 재배송과 환불 중 어떻게 처리되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.639399999694433,
  "retrievalMs": 2.982599999086233,
  "hits": [
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8908002376556396,
      "score": 0.8908002376556396
    },
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "denseScore": 0.8796849846839905,
      "score": 0.8796849846839905
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8746287822723389,
      "score": 0.8746287822723389
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8735221028327942,
      "score": 0.8735221028327942
    },
    {
      "chunkId": "knowledge-4-51cb0c17cf3cdfa6741c0b1d033e4ba3e4c8106c0482525c2635f571cf543e29",
      "denseScore": 0.8712007999420166,
      "score": 0.8712007999420166
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8908002376556396,
      "score": 0.8908002376556396
    },
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "denseScore": 0.8796849846839905,
      "score": 0.8796849846839905
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8746287822723389,
      "score": 0.8746287822723389
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8735221028327942,
      "score": 0.8735221028327942
    },
    {
      "chunkId": "knowledge-4-51cb0c17cf3cdfa6741c0b1d033e4ba3e4c8106c0482525c2635f571cf543e29",
      "denseScore": 0.8712007999420166,
      "score": 0.8712007999420166
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
        "denseScore": 0.8908002376556396,
        "score": 0.8908002376556396
      },
      {
        "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
        "denseScore": 0.8796849846839905,
        "score": 0.8796849846839905
      },
      {
        "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
        "denseScore": 0.8746287822723389,
        "score": 0.8746287822723389
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8735221028327942,
        "score": 0.8735221028327942
      },
      {
        "chunkId": "knowledge-4-51cb0c17cf3cdfa6741c0b1d033e4ba3e4c8106c0482525c2635f571cf543e29",
        "denseScore": 0.8712007999420166,
        "score": 0.8712007999420166
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1352,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "DLV-POL-ABSENCE-002",
        "anchor": "재배송하지 않고 부분 환불",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "originHit": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286"
    },
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "originHit": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818"
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "originHit": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-4-51cb0c17cf3cdfa6741c0b1d033e4ba3e4c8106c0482525c2635f571cf543e29",
      "originHit": "knowledge-4-51cb0c17cf3cdfa6741c0b1d033e4ba3e4c8106c0482525c2635f571cf543e29"
    }
  ]
}
```

## Q095

고객이 볼 수 있는 고객센터 데이터는 무엇인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-RBAC-001",
      "anchor": "본인 상담",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 121,
          "quote": "- 본인 상담"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q095",
  "group": "G048",
  "question": "고객이 볼 수 있는 고객센터 데이터는 무엇인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.939800000211108,
  "retrievalMs": 2.1629000002576504,
  "hits": [
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8583396077156067,
      "score": 0.8583396077156067
    },
    {
      "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
      "denseScore": 0.828821063041687,
      "score": 0.828821063041687
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.8285529017448425,
      "score": 0.8285529017448425
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.8262505531311035,
      "score": 0.8262505531311035
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8260294198989868,
      "score": 0.8260294198989868
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8583396077156067,
      "score": 0.8583396077156067
    },
    {
      "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
      "denseScore": 0.828821063041687,
      "score": 0.828821063041687
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.8285529017448425,
      "score": 0.8285529017448425
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.8262505531311035,
      "score": 0.8262505531311035
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8260294198989868,
      "score": 0.8260294198989868
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8583396077156067,
        "score": 0.8583396077156067
      },
      {
        "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
        "denseScore": 0.828821063041687,
        "score": 0.828821063041687
      },
      {
        "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
        "denseScore": 0.8285529017448425,
        "score": 0.8285529017448425
      },
      {
        "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
        "denseScore": 0.8262505531311035,
        "score": 0.8262505531311035
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8260294198989868,
        "score": 0.8260294198989868
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 582,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-RBAC-001",
        "anchor": "본인 상담",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    },
    {
      "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
      "originHit": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6"
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "originHit": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78"
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "originHit": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    }
  ]
}
```

## Q096

상담과 문의는 어떤 사용자 범위까지 열람 가능한가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-RBAC-001",
      "anchor": "본인 상담",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 121,
          "quote": "- 본인 상담"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q096",
  "group": "G048",
  "question": "상담과 문의는 어떤 사용자 범위까지 열람 가능한가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.66909999847121,
  "retrievalMs": 2.442400000290945,
  "hits": [
    {
      "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
      "denseScore": 0.8689297437667847,
      "score": 0.8689297437667847
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8577291369438171,
      "score": 0.8577291369438171
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8567509651184082,
      "score": 0.8567509651184082
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8522161245346069,
      "score": 0.8522161245346069
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "denseScore": 0.8400896191596985,
      "score": 0.8400896191596985
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
      "denseScore": 0.8689297437667847,
      "score": 0.8689297437667847
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8577291369438171,
      "score": 0.8577291369438171
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8567509651184082,
      "score": 0.8567509651184082
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8522161245346069,
      "score": 0.8522161245346069
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "denseScore": 0.8400896191596985,
      "score": 0.8400896191596985
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
        "denseScore": 0.8689297437667847,
        "score": 0.8689297437667847
      },
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.8577291369438171,
        "score": 0.8577291369438171
      },
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8567509651184082,
        "score": 0.8567509651184082
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8522161245346069,
        "score": 0.8522161245346069
      },
      {
        "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
        "denseScore": 0.8400896191596985,
        "score": 0.8400896191596985
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 674,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-RBAC-001",
        "anchor": "본인 상담",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
      "originHit": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805"
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "originHit": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c"
    }
  ]
}
```

## Q097

종료된 상담에 추가 문의하려면 어떻게 하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-CON-001",
      "anchor": "새로운 상담",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 204,
          "quote": "종료된 상담에서 추가 문의가 필요하면 기존 상담을 재개하지 않고 새로운 상담을 생성한다. `MUST`"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q097",
  "group": "G049",
  "question": "종료된 상담에 추가 문의하려면 어떻게 하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.924700000032317,
  "retrievalMs": 2.414100001260522,
  "hits": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.9178552031517029,
      "score": 0.9178552031517029
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8582707643508911,
      "score": 0.8582707643508911
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "denseScore": 0.8417186141014099,
      "score": 0.8417186141014099
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8409324884414673,
      "score": 0.8409324884414673
    },
    {
      "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
      "denseScore": 0.8403125405311584,
      "score": 0.8403125405311584
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.9178552031517029,
      "score": 0.9178552031517029
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8582707643508911,
      "score": 0.8582707643508911
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "denseScore": 0.8417186141014099,
      "score": 0.8417186141014099
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8409324884414673,
      "score": 0.8409324884414673
    },
    {
      "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
      "denseScore": 0.8403125405311584,
      "score": 0.8403125405311584
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.9178552031517029,
        "score": 0.9178552031517029
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8582707643508911,
        "score": 0.8582707643508911
      },
      {
        "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
        "denseScore": 0.8417186141014099,
        "score": 0.8417186141014099
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.8409324884414673,
        "score": 0.8409324884414673
      },
      {
        "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
        "denseScore": 0.8403125405311584,
        "score": 0.8403125405311584
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 704,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-CON-001",
        "anchor": "새로운 상담",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "originHit": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    },
    {
      "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
      "originHit": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd"
    }
  ]
}
```

## Q098

상담을 닫은 뒤 질문이 생기면 기존 상담을 다시 여나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-CON-001",
      "anchor": "새로운 상담",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 204,
          "quote": "종료된 상담에서 추가 문의가 필요하면 기존 상담을 재개하지 않고 새로운 상담을 생성한다. `MUST`"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q098",
  "group": "G049",
  "question": "상담을 닫은 뒤 질문이 생기면 기존 상담을 다시 여나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.148499999762862,
  "retrievalMs": 2.3422999984177295,
  "hits": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8999261856079102,
      "score": 0.8999261856079102
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8695216178894043,
      "score": 0.8695216178894043
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8478203415870667,
      "score": 0.8478203415870667
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8446136713027954,
      "score": 0.8446136713027954
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.843066394329071,
      "score": 0.843066394329071
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8999261856079102,
      "score": 0.8999261856079102
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8695216178894043,
      "score": 0.8695216178894043
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8478203415870667,
      "score": 0.8478203415870667
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8446136713027954,
      "score": 0.8446136713027954
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.843066394329071,
      "score": 0.843066394329071
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.8999261856079102,
        "score": 0.8999261856079102
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8695216178894043,
        "score": 0.8695216178894043
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8478203415870667,
        "score": 0.8478203415870667
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8446136713027954,
        "score": 0.8446136713027954
      },
      {
        "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
        "denseScore": 0.843066394329071,
        "score": 0.843066394329071
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1011,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-CON-001",
        "anchor": "새로운 상담",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "originHit": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c"
    }
  ]
}
```

## Q103

종료한 품질 문의에 추가 처리가 필요하면 재개하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-QI-002",
      "anchor": "새로운 품질 문의",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 632,
          "quote": "- `CLOSED` 이후 추가 처리가 필요하면 새로운 품질 문의를 생성한다. `MUST`"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q103",
  "group": "G052",
  "question": "종료한 품질 문의에 추가 처리가 필요하면 재개하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.430000000473228,
  "retrievalMs": 2.5141000005532987,
  "hits": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8870914578437805,
      "score": 0.8870914578437805
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8607237339019775,
      "score": 0.8607237339019775
    },
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "denseScore": 0.8596005439758301,
      "score": 0.8596005439758301
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8591673970222473,
      "score": 0.8591673970222473
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8585137128829956,
      "score": 0.8585137128829956
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8870914578437805,
      "score": 0.8870914578437805
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8607237339019775,
      "score": 0.8607237339019775
    },
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "denseScore": 0.8596005439758301,
      "score": 0.8596005439758301
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8591673970222473,
      "score": 0.8591673970222473
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8585137128829956,
      "score": 0.8585137128829956
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.8870914578437805,
        "score": 0.8870914578437805
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8607237339019775,
        "score": 0.8607237339019775
      },
      {
        "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
        "denseScore": 0.8596005439758301,
        "score": 0.8596005439758301
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8591673970222473,
        "score": 0.8591673970222473
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.8585137128829956,
        "score": 0.8585137128829956
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 822,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-QI-002",
        "anchor": "새로운 품질 문의",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "originHit": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    }
  ]
}
```

## Q104

품질 문의가 CLOSED인데 다시 문제가 생기면 어떻게 하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-QI-002",
      "anchor": "새로운 품질 문의",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 632,
          "quote": "- `CLOSED` 이후 추가 처리가 필요하면 새로운 품질 문의를 생성한다. `MUST`"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q104",
  "group": "G052",
  "question": "품질 문의가 CLOSED인데 다시 문제가 생기면 어떻게 하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.254299999767682,
  "retrievalMs": 2.281099999891012,
  "hits": [
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8812378644943237,
      "score": 0.8812378644943237
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8711088299751282,
      "score": 0.8711088299751282
    },
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "denseScore": 0.8686724305152893,
      "score": 0.8686724305152893
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "denseScore": 0.8677281737327576,
      "score": 0.8677281737327576
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8591477870941162,
      "score": 0.8591477870941162
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8812378644943237,
      "score": 0.8812378644943237
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8711088299751282,
      "score": 0.8711088299751282
    },
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "denseScore": 0.8686724305152893,
      "score": 0.8686724305152893
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "denseScore": 0.8677281737327576,
      "score": 0.8677281737327576
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8591477870941162,
      "score": 0.8591477870941162
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8812378644943237,
        "score": 0.8812378644943237
      },
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.8711088299751282,
        "score": 0.8711088299751282
      },
      {
        "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
        "denseScore": 0.8686724305152893,
        "score": 0.8686724305152893
      },
      {
        "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
        "denseScore": 0.8677281737327576,
        "score": 0.8677281737327576
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8591477870941162,
        "score": 0.8591477870941162
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 769,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-QI-002",
        "anchor": "새로운 품질 문의",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "originHit": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2"
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "originHit": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    }
  ]
}
```

## Q105

품질 문의를 등록하면 바로 환불 승인이 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-QI-003",
      "anchor": "의미하지 않는다",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 638,
          "quote": "- 품질 문의 등록 자체가 환불·재배송·배송 변경·구독 상태 변경을 의미하지 않는다. `MUST`"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q105",
  "group": "G053",
  "question": "품질 문의를 등록하면 바로 환불 승인이 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.75959999980114,
  "retrievalMs": 2.2986000003584195,
  "hits": [
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "denseScore": 0.8690419793128967,
      "score": 0.8690419793128967
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "denseScore": 0.8527994155883789,
      "score": 0.8527994155883789
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.851418137550354,
      "score": 0.851418137550354
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8464534282684326,
      "score": 0.8464534282684326
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8455385565757751,
      "score": 0.8455385565757751
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "denseScore": 0.8690419793128967,
      "score": 0.8690419793128967
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "denseScore": 0.8527994155883789,
      "score": 0.8527994155883789
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.851418137550354,
      "score": 0.851418137550354
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8464534282684326,
      "score": 0.8464534282684326
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8455385565757751,
      "score": 0.8455385565757751
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
        "denseScore": 0.8690419793128967,
        "score": 0.8690419793128967
      },
      {
        "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
        "denseScore": 0.8527994155883789,
        "score": 0.8527994155883789
      },
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.851418137550354,
        "score": 0.851418137550354
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8464534282684326,
        "score": 0.8464534282684326
      },
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8455385565757751,
        "score": 0.8455385565757751
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1087,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-QI-003",
        "anchor": "의미하지 않는다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2",
      "originHit": "knowledge-6-a126f7bcc08dc61c8c9b6257ef6ed792e564586e7823dd3403a559d3ea8ef7b2"
    },
    {
      "chunkId": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c",
      "originHit": "knowledge-6-a5a90435ab9a33ae0aff74507b0b78249ecc23467001c7e8baab53b1e99d148c"
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    }
  ]
}
```

## Q106

파손 문의를 접수한 것만으로 재배송이 확정되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-QI-003",
      "anchor": "의미하지 않는다",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 638,
          "quote": "- 품질 문의 등록 자체가 환불·재배송·배송 변경·구독 상태 변경을 의미하지 않는다. `MUST`"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q106",
  "group": "G053",
  "question": "파손 문의를 접수한 것만으로 재배송이 확정되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.902699999860488,
  "retrievalMs": 2.9840000006515766,
  "hits": [
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "denseScore": 0.8553077578544617,
      "score": 0.8553077578544617
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.8552678823471069,
      "score": 0.8552678823471069
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8538448214530945,
      "score": 0.8538448214530945
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.853277325630188,
      "score": 0.853277325630188
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8531050086021423,
      "score": 0.8531050086021423
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "denseScore": 0.8553077578544617,
      "score": 0.8553077578544617
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.8552678823471069,
      "score": 0.8552678823471069
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8538448214530945,
      "score": 0.8538448214530945
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.853277325630188,
      "score": 0.853277325630188
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8531050086021423,
      "score": 0.8531050086021423
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
        "denseScore": 0.8553077578544617,
        "score": 0.8553077578544617
      },
      {
        "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
        "denseScore": 0.8552678823471069,
        "score": 0.8552678823471069
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8538448214530945,
        "score": 0.8538448214530945
      },
      {
        "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
        "denseScore": 0.853277325630188,
        "score": 0.853277325630188
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8531050086021423,
        "score": 0.8531050086021423
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1748,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-QI-003",
        "anchor": "의미하지 않는다",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 5,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "originHit": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805"
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "originHit": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "originHit": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    }
  ]
}
```

## Q115

품질 문의에 11MB 사진을 첨부해도 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-FILE-003",
      "anchor": "10MB",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 945,
          "quote": "| 파일당 최대 크기 | `10MB` |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q115",
  "group": "G058",
  "question": "품질 문의에 11MB 사진을 첨부해도 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.926900000413298,
  "retrievalMs": 2.2088999994593905,
  "hits": [
    {
      "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
      "denseScore": 0.850938618183136,
      "score": 0.850938618183136
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8450937867164612,
      "score": 0.8450937867164612
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8449976444244385,
      "score": 0.8449976444244385
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8443352580070496,
      "score": 0.8443352580070496
    },
    {
      "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
      "denseScore": 0.8434270620346069,
      "score": 0.8434270620346069
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
      "denseScore": 0.850938618183136,
      "score": 0.850938618183136
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8450937867164612,
      "score": 0.8450937867164612
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8449976444244385,
      "score": 0.8449976444244385
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8443352580070496,
      "score": 0.8443352580070496
    },
    {
      "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
      "denseScore": 0.8434270620346069,
      "score": 0.8434270620346069
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
        "denseScore": 0.850938618183136,
        "score": 0.850938618183136
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8450937867164612,
        "score": 0.8450937867164612
      },
      {
        "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
        "denseScore": 0.8449976444244385,
        "score": 0.8449976444244385
      },
      {
        "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
        "denseScore": 0.8443352580070496,
        "score": 0.8443352580070496
      },
      {
        "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
        "denseScore": 0.8434270620346069,
        "score": 0.8434270620346069
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 889,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-FILE-003",
        "anchor": "10MB",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
      "originHit": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "originHit": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9"
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "originHit": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7"
    },
    {
      "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
      "originHit": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59"
    }
  ]
}
```

## Q116

문의 증빙 파일이 10MB를 넘으면 허용되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "CS-POL-FILE-003",
      "anchor": "10MB",
      "sources": [
        {
          "source": "Customer-Service/챱챱_Customer_Service_통합_정책서.md",
          "line": 945,
          "quote": "| 파일당 최대 크기 | `10MB` |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q116",
  "group": "G058",
  "question": "문의 증빙 파일이 10MB를 넘으면 허용되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.387399999875925,
  "retrievalMs": 1.8901999992522178,
  "hits": [
    {
      "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
      "denseScore": 0.862119197845459,
      "score": 0.862119197845459
    },
    {
      "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
      "denseScore": 0.844992995262146,
      "score": 0.844992995262146
    },
    {
      "chunkId": "knowledge-6-2745b2cf2cedae83902187859eaa8ca80883a1ff589868b737d899eeaa9a3da8",
      "denseScore": 0.8410556316375732,
      "score": 0.8410556316375732
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8374509215354919,
      "score": 0.8374509215354919
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8353032469749451,
      "score": 0.8353032469749451
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
      "denseScore": 0.862119197845459,
      "score": 0.862119197845459
    },
    {
      "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
      "denseScore": 0.844992995262146,
      "score": 0.844992995262146
    },
    {
      "chunkId": "knowledge-6-2745b2cf2cedae83902187859eaa8ca80883a1ff589868b737d899eeaa9a3da8",
      "denseScore": 0.8410556316375732,
      "score": 0.8410556316375732
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8374509215354919,
      "score": 0.8374509215354919
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8353032469749451,
      "score": 0.8353032469749451
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
        "denseScore": 0.862119197845459,
        "score": 0.862119197845459
      },
      {
        "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
        "denseScore": 0.844992995262146,
        "score": 0.844992995262146
      },
      {
        "chunkId": "knowledge-6-2745b2cf2cedae83902187859eaa8ca80883a1ff589868b737d899eeaa9a3da8",
        "denseScore": 0.8410556316375732,
        "score": 0.8410556316375732
      },
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.8374509215354919,
        "score": 0.8374509215354919
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8353032469749451,
        "score": 0.8353032469749451
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 469,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "CS-POL-FILE-003",
        "anchor": "10MB",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760",
      "originHit": "knowledge-6-66e7af9bebb0d0d155701040929c05cd346365e716b3e3c2c1458eb0dc9e8760"
    },
    {
      "chunkId": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59",
      "originHit": "knowledge-7-d29dbe7c6a95748ab4568afdee306f4803f8b8ecc0738e76f2ffbfd1bff88a59"
    },
    {
      "chunkId": "knowledge-6-2745b2cf2cedae83902187859eaa8ca80883a1ff589868b737d899eeaa9a3da8",
      "originHit": "knowledge-6-2745b2cf2cedae83902187859eaa8ca80883a1ff589868b737d899eeaa9a3da8"
    },
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    }
  ]
}
```

## Q121

만 13세 고객은 회원가입을 완료할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-SIGN-005",
      "anchor": "만 14세 미만",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 247,
          "quote": "- 만 14세 미만이면 가입을 완료하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q121",
  "group": "G061",
  "question": "만 13세 고객은 회원가입을 완료할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.754099999758182,
  "retrievalMs": 2.5782000011531636,
  "hits": [
    {
      "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
      "denseScore": 0.8659810423851013,
      "score": 0.8659810423851013
    },
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "denseScore": 0.8524894118309021,
      "score": 0.8524894118309021
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "denseScore": 0.847379744052887,
      "score": 0.847379744052887
    },
    {
      "chunkId": "knowledge-7-dfea7d93cdb02f07d8efbc35b58b9742dbd35a2637cc4217d096f93ae736026f",
      "denseScore": 0.8447490930557251,
      "score": 0.8447490930557251
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8428804874420166,
      "score": 0.8428804874420166
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
      "denseScore": 0.8659810423851013,
      "score": 0.8659810423851013
    },
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "denseScore": 0.8524894118309021,
      "score": 0.8524894118309021
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "denseScore": 0.847379744052887,
      "score": 0.847379744052887
    },
    {
      "chunkId": "knowledge-7-dfea7d93cdb02f07d8efbc35b58b9742dbd35a2637cc4217d096f93ae736026f",
      "denseScore": 0.8447490930557251,
      "score": 0.8447490930557251
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8428804874420166,
      "score": 0.8428804874420166
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
        "denseScore": 0.8659810423851013,
        "score": 0.8659810423851013
      },
      {
        "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
        "denseScore": 0.8524894118309021,
        "score": 0.8524894118309021
      },
      {
        "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
        "denseScore": 0.847379744052887,
        "score": 0.847379744052887
      },
      {
        "chunkId": "knowledge-7-dfea7d93cdb02f07d8efbc35b58b9742dbd35a2637cc4217d096f93ae736026f",
        "denseScore": 0.8447490930557251,
        "score": 0.8447490930557251
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8428804874420166,
        "score": 0.8428804874420166
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1207,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-SIGN-005",
        "anchor": "만 14세 미만",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
      "originHit": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9"
    },
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "originHit": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514"
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "originHit": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5"
    },
    {
      "chunkId": "knowledge-7-dfea7d93cdb02f07d8efbc35b58b9742dbd35a2637cc4217d096f93ae736026f",
      "originHit": "knowledge-7-dfea7d93cdb02f07d8efbc35b58b9742dbd35a2637cc4217d096f93ae736026f"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    }
  ]
}
```

## Q122

14세 생일 전이라도 가입할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-SIGN-005",
      "anchor": "만 14세 미만",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 247,
          "quote": "- 만 14세 미만이면 가입을 완료하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q122",
  "group": "G061",
  "question": "14세 생일 전이라도 가입할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.65760000165028,
  "retrievalMs": 2.110800000082236,
  "hits": [
    {
      "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
      "denseScore": 0.8791301846504211,
      "score": 0.8791301846504211
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8293013572692871,
      "score": 0.8293013572692871
    },
    {
      "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
      "denseScore": 0.8275503516197205,
      "score": 0.8275503516197205
    },
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "denseScore": 0.8259822130203247,
      "score": 0.8259822130203247
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8223257660865784,
      "score": 0.8223257660865784
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
      "denseScore": 0.8791301846504211,
      "score": 0.8791301846504211
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8293013572692871,
      "score": 0.8293013572692871
    },
    {
      "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
      "denseScore": 0.8275503516197205,
      "score": 0.8275503516197205
    },
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "denseScore": 0.8259822130203247,
      "score": 0.8259822130203247
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8223257660865784,
      "score": 0.8223257660865784
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
        "denseScore": 0.8791301846504211,
        "score": 0.8791301846504211
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8293013572692871,
        "score": 0.8293013572692871
      },
      {
        "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
        "denseScore": 0.8275503516197205,
        "score": 0.8275503516197205
      },
      {
        "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
        "denseScore": 0.8259822130203247,
        "score": 0.8259822130203247
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8223257660865784,
        "score": 0.8223257660865784
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 536,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-SIGN-005",
        "anchor": "만 14세 미만",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9",
      "originHit": "knowledge-7-fe28aaf9ca89c04826703b3c6caa78586655b6574e9c26fbec92a1fcbcd7fff9"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
      "originHit": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33"
    },
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "originHit": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    }
  ]
}
```

## Q125

한 기기에서 로그아웃하면 모든 기기에서 로그아웃되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-SES-003",
      "anchor": "현재 기기·브라우저 세션",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 280,
          "quote": "| 로그아웃 | 현재 기기·브라우저 세션 |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q125",
  "group": "G063",
  "question": "한 기기에서 로그아웃하면 모든 기기에서 로그아웃되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.104399998861481,
  "retrievalMs": 2.832699999999022,
  "hits": [
    {
      "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
      "denseScore": 0.8454777002334595,
      "score": 0.8454777002334595
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8440542221069336,
      "score": 0.8440542221069336
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8430966138839722,
      "score": 0.8430966138839722
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8398593664169312,
      "score": 0.8398593664169312
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "denseScore": 0.8377748131752014,
      "score": 0.8377748131752014
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
      "denseScore": 0.8454777002334595,
      "score": 0.8454777002334595
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8440542221069336,
      "score": 0.8440542221069336
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8430966138839722,
      "score": 0.8430966138839722
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8398593664169312,
      "score": 0.8398593664169312
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "denseScore": 0.8377748131752014,
      "score": 0.8377748131752014
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
        "denseScore": 0.8454777002334595,
        "score": 0.8454777002334595
      },
      {
        "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
        "denseScore": 0.8440542221069336,
        "score": 0.8440542221069336
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8430966138839722,
        "score": 0.8430966138839722
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.8398593664169312,
        "score": 0.8398593664169312
      },
      {
        "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
        "denseScore": 0.8377748131752014,
        "score": 0.8377748131752014
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1365,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-SES-003",
        "anchor": "현재 기기·브라우저 세션",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
      "originHit": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978"
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "originHit": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "originHit": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02"
    }
  ]
}
```

## Q126

현재 브라우저에서 로그아웃할 때 폐기되는 세션 범위는 어디까지인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-SES-003",
      "anchor": "현재 기기·브라우저 세션",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 280,
          "quote": "| 로그아웃 | 현재 기기·브라우저 세션 |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q126",
  "group": "G063",
  "question": "현재 브라우저에서 로그아웃할 때 폐기되는 세션 범위는 어디까지인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.246800000662915,
  "retrievalMs": 2.048699998340453,
  "hits": [
    {
      "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
      "denseScore": 0.8725960850715637,
      "score": 0.8725960850715637
    },
    {
      "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
      "denseScore": 0.8536322712898254,
      "score": 0.8536322712898254
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8353750705718994,
      "score": 0.8353750705718994
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8352028131484985,
      "score": 0.8352028131484985
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8299627304077148,
      "score": 0.8299627304077148
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
      "denseScore": 0.8725960850715637,
      "score": 0.8725960850715637
    },
    {
      "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
      "denseScore": 0.8536322712898254,
      "score": 0.8536322712898254
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8353750705718994,
      "score": 0.8353750705718994
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8352028131484985,
      "score": 0.8352028131484985
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8299627304077148,
      "score": 0.8299627304077148
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
        "denseScore": 0.8725960850715637,
        "score": 0.8725960850715637
      },
      {
        "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
        "denseScore": 0.8536322712898254,
        "score": 0.8536322712898254
      },
      {
        "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
        "denseScore": 0.8353750705718994,
        "score": 0.8353750705718994
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8352028131484985,
        "score": 0.8352028131484985
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.8299627304077148,
        "score": 0.8299627304077148
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 649,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-SES-003",
        "anchor": "현재 기기·브라우저 세션",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978",
      "originHit": "knowledge-7-695017764db24e1053bfab521b3df464edb1dd0d74cee329c1e165ff8badd978"
    },
    {
      "chunkId": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33",
      "originHit": "knowledge-7-89e8a507c48421f8ef3b41893e72f20704ee9654d145e4e4e5c10e4695819a33"
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "originHit": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    }
  ]
}
```

## Q129

마케팅 약관 버전이 바뀌어도 예전 동의가 그대로 적용되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-CNS-004",
      "anchor": "과거 동의를 자동 승계하지 않는다",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 389,
          "quote": "- 새 마케팅 Version은 과거 동의를 자동 승계하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q129",
  "group": "G065",
  "question": "마케팅 약관 버전이 바뀌어도 예전 동의가 그대로 적용되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.524500001542037,
  "retrievalMs": 2.8715999997075414,
  "hits": [
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "denseScore": 0.8742849826812744,
      "score": 0.8742849826812744
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "denseScore": 0.8648873567581177,
      "score": 0.8648873567581177
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8547444343566895,
      "score": 0.8547444343566895
    },
    {
      "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
      "denseScore": 0.850000262260437,
      "score": 0.850000262260437
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8458793759346008,
      "score": 0.8458793759346008
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "denseScore": 0.8742849826812744,
      "score": 0.8742849826812744
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "denseScore": 0.8648873567581177,
      "score": 0.8648873567581177
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8547444343566895,
      "score": 0.8547444343566895
    },
    {
      "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
      "denseScore": 0.850000262260437,
      "score": 0.850000262260437
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8458793759346008,
      "score": 0.8458793759346008
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
        "denseScore": 0.8742849826812744,
        "score": 0.8742849826812744
      },
      {
        "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
        "denseScore": 0.8648873567581177,
        "score": 0.8648873567581177
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8547444343566895,
        "score": 0.8547444343566895
      },
      {
        "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
        "denseScore": 0.850000262260437,
        "score": 0.850000262260437
      },
      {
        "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
        "denseScore": 0.8458793759346008,
        "score": 0.8458793759346008
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1163,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-CNS-004",
        "anchor": "과거 동의를 자동 승계하지 않는다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "originHit": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514"
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "originHit": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
      "originHit": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b"
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "originHit": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f"
    }
  ]
}
```

## Q130

새 이메일 마케팅 버전에 이전 동의를 자동으로 이어 쓰나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-CNS-004",
      "anchor": "과거 동의를 자동 승계하지 않는다",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 389,
          "quote": "- 새 마케팅 Version은 과거 동의를 자동 승계하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q130",
  "group": "G065",
  "question": "새 이메일 마케팅 버전에 이전 동의를 자동으로 이어 쓰나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.959199998978875,
  "retrievalMs": 2.304800000274554,
  "hits": [
    {
      "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
      "denseScore": 0.8863556385040283,
      "score": 0.8863556385040283
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8628239035606384,
      "score": 0.8628239035606384
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8558305501937866,
      "score": 0.8558305501937866
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "denseScore": 0.8549784421920776,
      "score": 0.8549784421920776
    },
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "denseScore": 0.8549171090126038,
      "score": 0.8549171090126038
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
      "denseScore": 0.8863556385040283,
      "score": 0.8863556385040283
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8628239035606384,
      "score": 0.8628239035606384
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8558305501937866,
      "score": 0.8558305501937866
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "denseScore": 0.8549784421920776,
      "score": 0.8549784421920776
    },
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "denseScore": 0.8549171090126038,
      "score": 0.8549171090126038
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
        "denseScore": 0.8863556385040283,
        "score": 0.8863556385040283
      },
      {
        "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
        "denseScore": 0.8628239035606384,
        "score": 0.8628239035606384
      },
      {
        "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
        "denseScore": 0.8558305501937866,
        "score": 0.8558305501937866
      },
      {
        "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
        "denseScore": 0.8549784421920776,
        "score": 0.8549784421920776
      },
      {
        "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
        "denseScore": 0.8549171090126038,
        "score": 0.8549171090126038
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 796,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-CNS-004",
        "anchor": "과거 동의를 자동 승계하지 않는다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b",
      "originHit": "knowledge-7-efe6fcdb7bdaabc180f4c0d0a97065062828507afeed9f99327182cfeec4a54b"
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "originHit": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132"
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "originHit": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f"
    },
    {
      "chunkId": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca",
      "originHit": "knowledge-1-89b65d31f59f6ce95de500582a864c681e2a991e15e0dcff3e0464683d59ecca"
    },
    {
      "chunkId": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514",
      "originHit": "knowledge-1-3c4e298b2dde2ad937deb007edff0c7d67e4b9222ab5a7d9f700a6ccad6ad514"
    }
  ]
}
```

## Q135

주소록 개인정보에 대한 요청은 어느 서비스가 담당하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-PRI-009",
      "anchor": "주소록·주소 상세",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 632,
          "quote": "| 주소록·주소 상세 | Subscription-Service |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q135",
  "group": "G068",
  "question": "주소록 개인정보에 대한 요청은 어느 서비스가 담당하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.825099998328369,
  "retrievalMs": 2.2926999990886543,
  "hits": [
    {
      "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
      "denseScore": 0.8423356413841248,
      "score": 0.8423356413841248
    },
    {
      "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
      "denseScore": 0.8415471315383911,
      "score": 0.8415471315383911
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8341272473335266,
      "score": 0.8341272473335266
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.832766056060791,
      "score": 0.832766056060791
    },
    {
      "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
      "denseScore": 0.8274092674255371,
      "score": 0.8274092674255371
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
      "denseScore": 0.8423356413841248,
      "score": 0.8423356413841248
    },
    {
      "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
      "denseScore": 0.8415471315383911,
      "score": 0.8415471315383911
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8341272473335266,
      "score": 0.8341272473335266
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.832766056060791,
      "score": 0.832766056060791
    },
    {
      "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
      "denseScore": 0.8274092674255371,
      "score": 0.8274092674255371
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
        "denseScore": 0.8423356413841248,
        "score": 0.8423356413841248
      },
      {
        "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
        "denseScore": 0.8415471315383911,
        "score": 0.8415471315383911
      },
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8341272473335266,
        "score": 0.8341272473335266
      },
      {
        "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
        "denseScore": 0.832766056060791,
        "score": 0.832766056060791
      },
      {
        "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
        "denseScore": 0.8274092674255371,
        "score": 0.8274092674255371
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 609,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-PRI-009",
        "anchor": "주소록·주소 상세",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
      "originHit": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668"
    },
    {
      "chunkId": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805",
      "originHit": "knowledge-7-55eaf25557a21e2d10090d740b3ac7754593b4e1ea2c7c23118bde35fc56d805"
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "originHit": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f"
    },
    {
      "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
      "originHit": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f"
    }
  ]
}
```

## Q136

주소 상세의 정정 요청을 담당하는 영역은 어디인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-PRI-009",
      "anchor": "주소록·주소 상세",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 632,
          "quote": "| 주소록·주소 상세 | Subscription-Service |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q136",
  "group": "G068",
  "question": "주소 상세의 정정 요청을 담당하는 영역은 어디인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.645499998849118,
  "retrievalMs": 2.2551000001840293,
  "hits": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8404747843742371,
      "score": 0.8404747843742371
    },
    {
      "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
      "denseScore": 0.8319764137268066,
      "score": 0.8319764137268066
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8208332061767578,
      "score": 0.8208332061767578
    },
    {
      "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
      "denseScore": 0.8158788084983826,
      "score": 0.8158788084983826
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8148808479309082,
      "score": 0.8148808479309082
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8404747843742371,
      "score": 0.8404747843742371
    },
    {
      "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
      "denseScore": 0.8319764137268066,
      "score": 0.8319764137268066
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8208332061767578,
      "score": 0.8208332061767578
    },
    {
      "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
      "denseScore": 0.8158788084983826,
      "score": 0.8158788084983826
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8148808479309082,
      "score": 0.8148808479309082
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
        "denseScore": 0.8404747843742371,
        "score": 0.8404747843742371
      },
      {
        "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
        "denseScore": 0.8319764137268066,
        "score": 0.8319764137268066
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8208332061767578,
        "score": 0.8208332061767578
      },
      {
        "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
        "denseScore": 0.8158788084983826,
        "score": 0.8158788084983826
      },
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8148808479309082,
        "score": 0.8148808479309082
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 609,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-PRI-009",
        "anchor": "주소록·주소 상세",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "originHit": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5"
    },
    {
      "chunkId": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668",
      "originHit": "knowledge-7-75f5b5b96c006706d781855fabfb5b39cf1bf0ec5f19c7212d16f5b750fa7668"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f",
      "originHit": "knowledge-7-8510b60642c289f85760d938a9fd648de051ffa3462841ddc903865ae134a89f"
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    }
  ]
}
```

## Q139

새 프로필 이미지 업로드에 실패하면 기존 사진도 사라지나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-OPS-001",
      "anchor": "기존 이미지 유지",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 852,
          "quote": "| MinIO 새 업로드 | 기존 이미지 유지 |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q139",
  "group": "G070",
  "question": "새 프로필 이미지 업로드에 실패하면 기존 사진도 사라지나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.675499999910244,
  "retrievalMs": 2.33969999862893,
  "hits": [
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8534369468688965,
      "score": 0.8534369468688965
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8484653830528259,
      "score": 0.8484653830528259
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8442577123641968,
      "score": 0.8442577123641968
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8404819369316101,
      "score": 0.8404819369316101
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8396634459495544,
      "score": 0.8396634459495544
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8534369468688965,
      "score": 0.8534369468688965
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8484653830528259,
      "score": 0.8484653830528259
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8442577123641968,
      "score": 0.8442577123641968
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8404819369316101,
      "score": 0.8404819369316101
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8396634459495544,
      "score": 0.8396634459495544
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
        "denseScore": 0.8534369468688965,
        "score": 0.8534369468688965
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8484653830528259,
        "score": 0.8484653830528259
      },
      {
        "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
        "denseScore": 0.8442577123641968,
        "score": 0.8442577123641968
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8404819369316101,
        "score": 0.8404819369316101
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8396634459495544,
        "score": 0.8396634459495544
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 755,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-OPS-001",
        "anchor": "기존 이미지 유지",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "originHit": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "originHit": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    }
  ]
}
```

## Q140

사진 교체 파일 업로드 실패 시 이전 이미지는 어떻게 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "AUTH-POL-OPS-001",
      "anchor": "기존 이미지 유지",
      "sources": [
        {
          "source": "Auth-Service/챱챱_Auth_Service_통합_정책서.md",
          "line": 852,
          "quote": "| MinIO 새 업로드 | 기존 이미지 유지 |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q140",
  "group": "G070",
  "question": "사진 교체 파일 업로드 실패 시 이전 이미지는 어떻게 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.96030000007886,
  "retrievalMs": 2.381500000410597,
  "hits": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8459763526916504,
      "score": 0.8459763526916504
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8447697162628174,
      "score": 0.8447697162628174
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8444148302078247,
      "score": 0.8444148302078247
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8426501750946045,
      "score": 0.8426501750946045
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8423932790756226,
      "score": 0.8423932790756226
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8459763526916504,
      "score": 0.8459763526916504
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8447697162628174,
      "score": 0.8447697162628174
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8444148302078247,
      "score": 0.8444148302078247
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8426501750946045,
      "score": 0.8426501750946045
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8423932790756226,
      "score": 0.8423932790756226
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8459763526916504,
        "score": 0.8459763526916504
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8447697162628174,
        "score": 0.8447697162628174
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8444148302078247,
        "score": 0.8444148302078247
      },
      {
        "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
        "denseScore": 0.8426501750946045,
        "score": 0.8426501750946045
      },
      {
        "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
        "denseScore": 0.8423932790756226,
        "score": 0.8423932790756226
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 784,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "AUTH-POL-OPS-001",
        "anchor": "기존 이미지 유지",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "originHit": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7"
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "originHit": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132"
    }
  ]
}
```

## Q141

시작 전날 14시 정각에 첫 구독 취소 요청을 보내도 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-003",
      "anchor": "14:00:00 KST",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 319,
          "quote": "- 첫 구독의 **대상 첫 이용 기간**은 시작일 전날 `14:00:00 KST`보다 이전에 서버가 취소 요청을 접수하고, 대상 기간 주문 중 전달 완료 주문이 하나도 없을 때만 전액 취소할 수 있다. `14:00:00 KST`부터는 취소·환불 요청을 거절한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 327,
          "quote": "- 결제 성공한 **대상 다음 이용 기간**은 시작일 전날 `14:00:00 KST`보다 이전에 서버가 해지 요청을 접수하고, 대상 기간 주문 중 전달 완료 주문이 하나도 없을 때만 전액 취소할 수 있다. `14:00:00 KST`부터는 해당 기간의 취소·전액 환불 요청을 거절한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q141",
  "group": "G071",
  "question": "시작 전날 14시 정각에 첫 구독 취소 요청을 보내도 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 13.180699999793433,
  "retrievalMs": 2.7387999998609303,
  "hits": [
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8920634984970093,
      "score": 0.8920634984970093
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8904459476470947,
      "score": 0.8904459476470947
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.889424741268158,
      "score": 0.889424741268158
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8776262998580933,
      "score": 0.8776262998580933
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "denseScore": 0.8757818341255188,
      "score": 0.8757818341255188
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8920634984970093,
      "score": 0.8920634984970093
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8904459476470947,
      "score": 0.8904459476470947
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.889424741268158,
      "score": 0.889424741268158
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8776262998580933,
      "score": 0.8776262998580933
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "denseScore": 0.8757818341255188,
      "score": 0.8757818341255188
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
        "denseScore": 0.8920634984970093,
        "score": 0.8920634984970093
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8904459476470947,
        "score": 0.8904459476470947
      },
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.889424741268158,
        "score": 0.889424741268158
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8776262998580933,
        "score": 0.8776262998580933
      },
      {
        "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
        "denseScore": 0.8757818341255188,
        "score": 0.8757818341255188
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1119,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-003",
        "anchor": "14:00:00 KST",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 1,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "originHit": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "originHit": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4"
    }
  ]
}
```

## Q142

첫 이용일 전날 오후 두 시가 된 순간에도 시작 취소가 가능한가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-003",
      "anchor": "14:00:00 KST",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 319,
          "quote": "- 첫 구독의 **대상 첫 이용 기간**은 시작일 전날 `14:00:00 KST`보다 이전에 서버가 취소 요청을 접수하고, 대상 기간 주문 중 전달 완료 주문이 하나도 없을 때만 전액 취소할 수 있다. `14:00:00 KST`부터는 취소·환불 요청을 거절한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 327,
          "quote": "- 결제 성공한 **대상 다음 이용 기간**은 시작일 전날 `14:00:00 KST`보다 이전에 서버가 해지 요청을 접수하고, 대상 기간 주문 중 전달 완료 주문이 하나도 없을 때만 전액 취소할 수 있다. `14:00:00 KST`부터는 해당 기간의 취소·전액 환불 요청을 거절한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q142",
  "group": "G071",
  "question": "첫 이용일 전날 오후 두 시가 된 순간에도 시작 취소가 가능한가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.270400000285008,
  "retrievalMs": 2.4157000007107854,
  "hits": [
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8847957849502563,
      "score": 0.8847957849502563
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8842959403991699,
      "score": 0.8842959403991699
    },
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "denseScore": 0.8823753595352173,
      "score": 0.8823753595352173
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8822897672653198,
      "score": 0.8822897672653198
    },
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "denseScore": 0.8799009919166565,
      "score": 0.8799009919166565
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8847957849502563,
      "score": 0.8847957849502563
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8842959403991699,
      "score": 0.8842959403991699
    },
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "denseScore": 0.8823753595352173,
      "score": 0.8823753595352173
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8822897672653198,
      "score": 0.8822897672653198
    },
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "denseScore": 0.8799009919166565,
      "score": 0.8799009919166565
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.8847957849502563,
        "score": 0.8847957849502563
      },
      {
        "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
        "denseScore": 0.8842959403991699,
        "score": 0.8842959403991699
      },
      {
        "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
        "denseScore": 0.8823753595352173,
        "score": 0.8823753595352173
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8822897672653198,
        "score": 0.8822897672653198
      },
      {
        "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
        "denseScore": 0.8799009919166565,
        "score": 0.8799009919166565
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1083,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-003",
        "anchor": "14:00:00 KST",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "originHit": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c"
    },
    {
      "chunkId": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f",
      "originHit": "knowledge-1-30f2373c699ad61444121d29b340b2c01f520a8cac9170f580500501e97aa78f"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805",
      "originHit": "knowledge-1-d8b9426a4e0ba9e419c0f2f4991fb33af34aef847f982c126e5f7469315f1805"
    }
  ]
}
```

## Q147

설정 변경 추가 결제가 실패하면 기존 주문도 없어지나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-002",
      "anchor": "기존 구독 설정과 주문을 유지",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 280,
          "quote": "- 추가 결제에 실패하면 미리 생성한 새 설정과 주문을 `변경 미적용` 상태로 바꾸고 기존 구독 설정과 주문을 유지한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 281,
          "quote": "- 여러 원 결제의 취소를 시작하기 전에 실패하면 미리 생성한 새 설정과 주문을 `변경 미적용` 상태로 바꾸고 기존 구독 설정과 주문을 유지하며, 고객에게 변경되지 않았음을 알린다. 첫 원 결제 취소부터 실패하면 같은 처리와 함께 해당 환불을 `실패`로 기록한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q147",
  "group": "G074",
  "question": "설정 변경 추가 결제가 실패하면 기존 주문도 없어지나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.290000000371947,
  "retrievalMs": 3.196699999534758,
  "hits": [
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.900420069694519,
      "score": 0.900420069694519
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8953807353973389,
      "score": 0.8953807353973389
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8915656805038452,
      "score": 0.8915656805038452
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8865209817886353,
      "score": 0.8865209817886353
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "denseScore": 0.8837928771972656,
      "score": 0.8837928771972656
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.900420069694519,
      "score": 0.900420069694519
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8953807353973389,
      "score": 0.8953807353973389
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8915656805038452,
      "score": 0.8915656805038452
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8865209817886353,
      "score": 0.8865209817886353
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "denseScore": 0.8837928771972656,
      "score": 0.8837928771972656
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
        "denseScore": 0.900420069694519,
        "score": 0.900420069694519
      },
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8953807353973389,
        "score": 0.8953807353973389
      },
      {
        "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
        "denseScore": 0.8915656805038452,
        "score": 0.8915656805038452
      },
      {
        "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
        "denseScore": 0.8865209817886353,
        "score": 0.8865209817886353
      },
      {
        "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
        "denseScore": 0.8837928771972656,
        "score": 0.8837928771972656
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1848,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-002",
        "anchor": "기존 구독 설정과 주문을 유지",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "originHit": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c"
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "originHit": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0"
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "originHit": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576"
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "originHit": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02"
    }
  ]
}
```

## Q148

변경 차액 결제 실패 시 이전 설정을 계속 사용하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-002",
      "anchor": "기존 구독 설정과 주문을 유지",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 280,
          "quote": "- 추가 결제에 실패하면 미리 생성한 새 설정과 주문을 `변경 미적용` 상태로 바꾸고 기존 구독 설정과 주문을 유지한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 281,
          "quote": "- 여러 원 결제의 취소를 시작하기 전에 실패하면 미리 생성한 새 설정과 주문을 `변경 미적용` 상태로 바꾸고 기존 구독 설정과 주문을 유지하며, 고객에게 변경되지 않았음을 알린다. 첫 원 결제 취소부터 실패하면 같은 처리와 함께 해당 환불을 `실패`로 기록한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q148",
  "group": "G074",
  "question": "변경 차액 결제 실패 시 이전 설정을 계속 사용하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.185699999259668,
  "retrievalMs": 2.6405000007798662,
  "hits": [
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8871667385101318,
      "score": 0.8871667385101318
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.8803845643997192,
      "score": 0.8803845643997192
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "denseScore": 0.8800082802772522,
      "score": 0.8800082802772522
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "denseScore": 0.8782804012298584,
      "score": 0.8782804012298584
    },
    {
      "chunkId": "knowledge-3-5b92b133b50a2d22fcc79bb41d3ec783e1038a0772802e0528393560a70a4ff0",
      "denseScore": 0.8753530979156494,
      "score": 0.8753530979156494
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8871667385101318,
      "score": 0.8871667385101318
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.8803845643997192,
      "score": 0.8803845643997192
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "denseScore": 0.8800082802772522,
      "score": 0.8800082802772522
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "denseScore": 0.8782804012298584,
      "score": 0.8782804012298584
    },
    {
      "chunkId": "knowledge-3-5b92b133b50a2d22fcc79bb41d3ec783e1038a0772802e0528393560a70a4ff0",
      "denseScore": 0.8753530979156494,
      "score": 0.8753530979156494
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8871667385101318,
        "score": 0.8871667385101318
      },
      {
        "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
        "denseScore": 0.8803845643997192,
        "score": 0.8803845643997192
      },
      {
        "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
        "denseScore": 0.8800082802772522,
        "score": 0.8800082802772522
      },
      {
        "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
        "denseScore": 0.8782804012298584,
        "score": 0.8782804012298584
      },
      {
        "chunkId": "knowledge-3-5b92b133b50a2d22fcc79bb41d3ec783e1038a0772802e0528393560a70a4ff0",
        "denseScore": 0.8753530979156494,
        "score": 0.8753530979156494
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1268,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-002",
        "anchor": "기존 구독 설정과 주문을 유지",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "originHit": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c"
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "originHit": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4"
    },
    {
      "chunkId": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02",
      "originHit": "knowledge-2-03a8fbddc55d16061c151fb7e34688486064bb7763e11c0c2622d30c76b11b02"
    },
    {
      "chunkId": "knowledge-3-5b92b133b50a2d22fcc79bb41d3ec783e1038a0772802e0528393560a70a4ff0",
      "originHit": "knowledge-3-5b92b133b50a2d22fcc79bb41d3ec783e1038a0772802e0528393560a70a4ff0"
    }
  ]
}
```

## Q153

이용 중인 구독의 현재 결제카드를 바로 삭제할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-011",
      "anchor": "현재 결제수단은 직접 삭제할 수 없다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 871,
          "quote": "- 진행 중 구독의 현재 결제수단은 직접 삭제할 수 없다. 다른 등록 수단을 현재 결제수단으로 선택한 뒤 이전 수단을 삭제하거나 구독이 완전히 종료된 뒤 삭제할 수 있다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q153",
  "group": "G077",
  "question": "이용 중인 구독의 현재 결제카드를 바로 삭제할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.807399999976042,
  "retrievalMs": 2.857100000255741,
  "hits": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8895953893661499,
      "score": 0.8895953893661499
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8882448673248291,
      "score": 0.8882448673248291
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "denseScore": 0.8771687746047974,
      "score": 0.8771687746047974
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8767207860946655,
      "score": 0.8767207860946655
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8750041127204895,
      "score": 0.8750041127204895
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8895953893661499,
      "score": 0.8895953893661499
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8882448673248291,
      "score": 0.8882448673248291
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "denseScore": 0.8771687746047974,
      "score": 0.8771687746047974
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8767207860946655,
      "score": 0.8767207860946655
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8750041127204895,
      "score": 0.8750041127204895
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.8895953893661499,
        "score": 0.8895953893661499
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8882448673248291,
        "score": 0.8882448673248291
      },
      {
        "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
        "denseScore": 0.8771687746047974,
        "score": 0.8771687746047974
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.8767207860946655,
        "score": 0.8767207860946655
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8750041127204895,
        "score": 0.8750041127204895
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1198,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-011",
        "anchor": "현재 결제수단은 직접 삭제할 수 없다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "originHit": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    }
  ]
}
```

## Q154

대체 카드 선택 없이 진행 중 구독의 현재 결제수단을 지워도 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-011",
      "anchor": "현재 결제수단은 직접 삭제할 수 없다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 871,
          "quote": "- 진행 중 구독의 현재 결제수단은 직접 삭제할 수 없다. 다른 등록 수단을 현재 결제수단으로 선택한 뒤 이전 수단을 삭제하거나 구독이 완전히 종료된 뒤 삭제할 수 있다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q154",
  "group": "G077",
  "question": "대체 카드 선택 없이 진행 중 구독의 현재 결제수단을 지워도 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.98430000092776,
  "retrievalMs": 2.4324000005435664,
  "hits": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.9165055155754089,
      "score": 0.9165055155754089
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.9047845602035522,
      "score": 0.9047845602035522
    },
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "denseScore": 0.9015272855758667,
      "score": 0.9015272855758667
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8943276405334473,
      "score": 0.8943276405334473
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8936961889266968,
      "score": 0.8936961889266968
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.9165055155754089,
      "score": 0.9165055155754089
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "denseScore": 0.9047845602035522,
      "score": 0.9047845602035522
    },
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "denseScore": 0.9015272855758667,
      "score": 0.9015272855758667
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8943276405334473,
      "score": 0.8943276405334473
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8936961889266968,
      "score": 0.8936961889266968
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.9165055155754089,
        "score": 0.9165055155754089
      },
      {
        "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
        "denseScore": 0.9047845602035522,
        "score": 0.9047845602035522
      },
      {
        "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
        "denseScore": 0.9015272855758667,
        "score": 0.9015272855758667
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8943276405334473,
        "score": 0.8943276405334473
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8936961889266968,
        "score": 0.8936961889266968
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1042,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-011",
        "anchor": "현재 결제수단은 직접 삭제할 수 없다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    },
    {
      "chunkId": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78",
      "originHit": "knowledge-3-73e1545d271fc7eb2cbb466baa0678997f2945a153b7a5a45e7ff587523c2d78"
    },
    {
      "chunkId": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2",
      "originHit": "knowledge-3-b2f887bd2f1effec2205c15ff77738fc81e167ef4508b1789601042c07f1d4a2"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    }
  ]
}
```

## Q159

여러 환불 중 일부만 성공했으면 완료 처리되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-012",
      "anchor": "확인 필요",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 909,
          "quote": "- 첫 원 결제 취소부터 실패하면 이후 원 결제의 취소를 실행하지 않고 환불을 `실패`로 기록한다. 하나 이상 성공한 뒤 다음 취소가 실패하면 이후 원 결제의 취소를 중단하고, 이미 성공한 취소는 되돌리지 않으며 환불 상태를 `확인 필요`로 바꾼다. 이때 성공·실패 거래와 남은 미처리 금액을 기록한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 914,
          "quote": "- 부분 성공 이후의 추가 처리와 완료 기능은 현재 프로젝트 범위에 포함하지 않는다. 성공·실패 거래와 미처리 금액을 보존하고 환불은 `확인 필요` 상태로 유지한다. `확인 필요`에서 남은 금액만 다시 취소하거나 완료로 바꾸는 기능은 기본 구현이 안정된 뒤 별도 고도화 과제로 검토한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 920,
          "quote": "월요일 주문에 최초 결제 A의 11,900원과 가장 최근 추가 결제 B의 8,900원이 배분되어 있다면 배송 건 환불 20,800원은 B에서 8,900원을 먼저 취소하고 A에서 11,900원을 취소한다. 정상 흐름에서는 두 취소가 모두 성공한다고 가정한다. 실제로 B 취소만 성공하고 A 취소가 실패하면 B의 성공 내역과 A의 실패 내역, 미처리 금액 11,900원을 보존하고 환불 상태를 `확인 필요`로 바꾼 뒤 현재 프로젝트에서는 추가 처리하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q159",
  "group": "G080",
  "question": "여러 환불 중 일부만 성공했으면 완료 처리되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.812000000441913,
  "retrievalMs": 2.7399999999033753,
  "hits": [
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "denseScore": 0.8712302446365356,
      "score": 0.8712302446365356
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.8692382574081421,
      "score": 0.8692382574081421
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8684701323509216,
      "score": 0.8684701323509216
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.8676475286483765,
      "score": 0.8676475286483765
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8656048774719238,
      "score": 0.8656048774719238
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "denseScore": 0.8712302446365356,
      "score": 0.8712302446365356
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.8692382574081421,
      "score": 0.8692382574081421
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8684701323509216,
      "score": 0.8684701323509216
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "denseScore": 0.8676475286483765,
      "score": 0.8676475286483765
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8656048774719238,
      "score": 0.8656048774719238
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
        "denseScore": 0.8712302446365356,
        "score": 0.8712302446365356
      },
      {
        "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
        "denseScore": 0.8692382574081421,
        "score": 0.8692382574081421
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8684701323509216,
        "score": 0.8684701323509216
      },
      {
        "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
        "denseScore": 0.8676475286483765,
        "score": 0.8676475286483765
      },
      {
        "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
        "denseScore": 0.8656048774719238,
        "score": 0.8656048774719238
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1388,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-012",
        "anchor": "확인 필요",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "originHit": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818"
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "originHit": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c",
      "originHit": "knowledge-2-d5a76835d3f2c1ecb0e74eff12f9db67ada00eeb3de014679f28e612d45e461c"
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "originHit": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576"
    }
  ]
}
```

## Q160

첫 카드 취소는 성공하고 다음 취소가 실패하면 환불 상태가 무엇인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-012",
      "anchor": "확인 필요",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 909,
          "quote": "- 첫 원 결제 취소부터 실패하면 이후 원 결제의 취소를 실행하지 않고 환불을 `실패`로 기록한다. 하나 이상 성공한 뒤 다음 취소가 실패하면 이후 원 결제의 취소를 중단하고, 이미 성공한 취소는 되돌리지 않으며 환불 상태를 `확인 필요`로 바꾼다. 이때 성공·실패 거래와 남은 미처리 금액을 기록한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 914,
          "quote": "- 부분 성공 이후의 추가 처리와 완료 기능은 현재 프로젝트 범위에 포함하지 않는다. 성공·실패 거래와 미처리 금액을 보존하고 환불은 `확인 필요` 상태로 유지한다. `확인 필요`에서 남은 금액만 다시 취소하거나 완료로 바꾸는 기능은 기본 구현이 안정된 뒤 별도 고도화 과제로 검토한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 920,
          "quote": "월요일 주문에 최초 결제 A의 11,900원과 가장 최근 추가 결제 B의 8,900원이 배분되어 있다면 배송 건 환불 20,800원은 B에서 8,900원을 먼저 취소하고 A에서 11,900원을 취소한다. 정상 흐름에서는 두 취소가 모두 성공한다고 가정한다. 실제로 B 취소만 성공하고 A 취소가 실패하면 B의 성공 내역과 A의 실패 내역, 미처리 금액 11,900원을 보존하고 환불 상태를 `확인 필요`로 바꾼 뒤 현재 프로젝트에서는 추가 처리하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q160",
  "group": "G080",
  "question": "첫 카드 취소는 성공하고 다음 취소가 실패하면 환불 상태가 무엇인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.974800001145923,
  "retrievalMs": 2.9232000015326776,
  "hits": [
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8843260407447815,
      "score": 0.8843260407447815
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8808760643005371,
      "score": 0.8808760643005371
    },
    {
      "chunkId": "knowledge-2-a420aeaaf0d42881b23abafac8641d504046982fb7e717ba23b37e88d03623b0",
      "denseScore": 0.8768125176429749,
      "score": 0.8768125176429749
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8753546476364136,
      "score": 0.8753546476364136
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8745606541633606,
      "score": 0.8745606541633606
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8843260407447815,
      "score": 0.8843260407447815
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.8808760643005371,
      "score": 0.8808760643005371
    },
    {
      "chunkId": "knowledge-2-a420aeaaf0d42881b23abafac8641d504046982fb7e717ba23b37e88d03623b0",
      "denseScore": 0.8768125176429749,
      "score": 0.8768125176429749
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8753546476364136,
      "score": 0.8753546476364136
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8745606541633606,
      "score": 0.8745606541633606
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
        "denseScore": 0.8843260407447815,
        "score": 0.8843260407447815
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.8808760643005371,
        "score": 0.8808760643005371
      },
      {
        "chunkId": "knowledge-2-a420aeaaf0d42881b23abafac8641d504046982fb7e717ba23b37e88d03623b0",
        "denseScore": 0.8768125176429749,
        "score": 0.8768125176429749
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8753546476364136,
        "score": 0.8753546476364136
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8745606541633606,
        "score": 0.8745606541633606
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1303,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-012",
        "anchor": "확인 필요",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "originHit": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-2-a420aeaaf0d42881b23abafac8641d504046982fb7e717ba23b37e88d03623b0",
      "originHit": "knowledge-2-a420aeaaf0d42881b23abafac8641d504046982fb7e717ba23b37e88d03623b0"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    }
  ]
}
```

## Q161

공휴일에 빠진 주문은 다음 날 대신 배송되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-006",
      "anchor": "다른 날짜로 옮기지 않는다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1040,
          "quote": "- 정책 내용: 일요일과 대한민국의 공식 공휴일·대체공휴일에는 주문을 생성하지 않는다. 해당 날짜의 주문을 다른 날짜로 옮기지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q161",
  "group": "G081",
  "question": "공휴일에 빠진 주문은 다음 날 대신 배송되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.069099998872844,
  "retrievalMs": 2.5128999986918643,
  "hits": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8863214254379272,
      "score": 0.8863214254379272
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8851874470710754,
      "score": 0.8851874470710754
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "denseScore": 0.8773449659347534,
      "score": 0.8773449659347534
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8762969970703125,
      "score": 0.8762969970703125
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8722091317176819,
      "score": 0.8722091317176819
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8863214254379272,
      "score": 0.8863214254379272
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8851874470710754,
      "score": 0.8851874470710754
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "denseScore": 0.8773449659347534,
      "score": 0.8773449659347534
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8762969970703125,
      "score": 0.8762969970703125
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8722091317176819,
      "score": 0.8722091317176819
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.8863214254379272,
        "score": 0.8863214254379272
      },
      {
        "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
        "denseScore": 0.8851874470710754,
        "score": 0.8851874470710754
      },
      {
        "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
        "denseScore": 0.8773449659347534,
        "score": 0.8773449659347534
      },
      {
        "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
        "denseScore": 0.8762969970703125,
        "score": 0.8762969970703125
      },
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8722091317176819,
        "score": 0.8722091317176819
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 458,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-006",
        "anchor": "다른 날짜로 옮기지 않는다",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "originHit": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80"
    },
    {
      "chunkId": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637",
      "originHit": "knowledge-1-20fc9eb1b66a10791b89e363870137a003577662e5b1b703266fe7aafbf9f637"
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "originHit": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94"
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    }
  ]
}
```

## Q162

휴일 배송을 다른 날짜로 옮겨서 받을 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ORDER-006",
      "anchor": "다른 날짜로 옮기지 않는다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1040,
          "quote": "- 정책 내용: 일요일과 대한민국의 공식 공휴일·대체공휴일에는 주문을 생성하지 않는다. 해당 날짜의 주문을 다른 날짜로 옮기지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q162",
  "group": "G081",
  "question": "휴일 배송을 다른 날짜로 옮겨서 받을 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.438599998451537,
  "retrievalMs": 2.2908999999344815,
  "hits": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8780138492584229,
      "score": 0.8780138492584229
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8714445233345032,
      "score": 0.8714445233345032
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8671541213989258,
      "score": 0.8671541213989258
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.866102933883667,
      "score": 0.866102933883667
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8653500080108643,
      "score": 0.8653500080108643
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.8780138492584229,
      "score": 0.8780138492584229
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "denseScore": 0.8714445233345032,
      "score": 0.8714445233345032
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "denseScore": 0.8671541213989258,
      "score": 0.8671541213989258
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.866102933883667,
      "score": 0.866102933883667
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8653500080108643,
      "score": 0.8653500080108643
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.8780138492584229,
        "score": 0.8780138492584229
      },
      {
        "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
        "denseScore": 0.8714445233345032,
        "score": 0.8714445233345032
      },
      {
        "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
        "denseScore": 0.8671541213989258,
        "score": 0.8671541213989258
      },
      {
        "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
        "denseScore": 0.866102933883667,
        "score": 0.866102933883667
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8653500080108643,
        "score": 0.8653500080108643
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 788,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ORDER-006",
        "anchor": "다른 날짜로 옮기지 않는다",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94",
      "originHit": "knowledge-1-b87185142475e025775ac7b203dc438e087da9c21fd921618c00966bca63ce94"
    },
    {
      "chunkId": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80",
      "originHit": "knowledge-1-dc00d50f3687e85ed2bb900c948a3aa3b5c27a7e09ec6d2aa0e088999d54af80"
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "originHit": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    }
  ]
}
```

## Q165

해지 예정인데 새 구독을 바로 신청할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-014",
      "anchor": "종료되기 전에는 새 구독을 시작할 수 없다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 564,
          "quote": "- 해지 예정 구독은 현재 이용 기간 마지막 날까지 진행 중 구독으로 유지하므로 종료되기 전에는 새 구독을 시작할 수 없다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q165",
  "group": "G083",
  "question": "해지 예정인데 새 구독을 바로 신청할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.385600000518025,
  "retrievalMs": 2.463799999532057,
  "hits": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8968344926834106,
      "score": 0.8968344926834106
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8948709964752197,
      "score": 0.8948709964752197
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8926427364349365,
      "score": 0.8926427364349365
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.8926404714584351,
      "score": 0.8926404714584351
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "denseScore": 0.8837321996688843,
      "score": 0.8837321996688843
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8968344926834106,
      "score": 0.8968344926834106
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8948709964752197,
      "score": 0.8948709964752197
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8926427364349365,
      "score": 0.8926427364349365
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.8926404714584351,
      "score": 0.8926404714584351
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "denseScore": 0.8837321996688843,
      "score": 0.8837321996688843
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
        "denseScore": 0.8968344926834106,
        "score": 0.8968344926834106
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8948709964752197,
        "score": 0.8948709964752197
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8926427364349365,
        "score": 0.8926427364349365
      },
      {
        "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
        "denseScore": 0.8926404714584351,
        "score": 0.8926404714584351
      },
      {
        "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
        "denseScore": 0.8837321996688843,
        "score": 0.8837321996688843
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 860,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-014",
        "anchor": "종료되기 전에는 새 구독을 시작할 수 없다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "originHit": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "originHit": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120"
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "originHit": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d"
    }
  ]
}
```

## Q166

현재 구독이 해지 예정 상태이면 다른 구독을 시작해도 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-014",
      "anchor": "종료되기 전에는 새 구독을 시작할 수 없다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 564,
          "quote": "- 해지 예정 구독은 현재 이용 기간 마지막 날까지 진행 중 구독으로 유지하므로 종료되기 전에는 새 구독을 시작할 수 없다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q166",
  "group": "G083",
  "question": "현재 구독이 해지 예정 상태이면 다른 구독을 시작해도 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.429300000600051,
  "retrievalMs": 2.516000000468921,
  "hits": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.9108235239982605,
      "score": 0.9108235239982605
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.9012734889984131,
      "score": 0.9012734889984131
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.9011752605438232,
      "score": 0.9011752605438232
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8960213661193848,
      "score": 0.8960213661193848
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "denseScore": 0.8954876661300659,
      "score": 0.8954876661300659
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.9108235239982605,
      "score": 0.9108235239982605
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.9012734889984131,
      "score": 0.9012734889984131
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.9011752605438232,
      "score": 0.9011752605438232
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8960213661193848,
      "score": 0.8960213661193848
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "denseScore": 0.8954876661300659,
      "score": 0.8954876661300659
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
        "denseScore": 0.9108235239982605,
        "score": 0.9108235239982605
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.9012734889984131,
        "score": 0.9012734889984131
      },
      {
        "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
        "denseScore": 0.9011752605438232,
        "score": 0.9011752605438232
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8960213661193848,
        "score": 0.8960213661193848
      },
      {
        "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
        "denseScore": 0.8954876661300659,
        "score": 0.8954876661300659
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 822,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-014",
        "anchor": "종료되기 전에는 새 구독을 시작할 수 없다",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "originHit": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "originHit": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "originHit": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c"
    }
  ]
}
```

## Q167

서울 주소를 배송지로 등록할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ADDRESS-001",
      "anchor": "대구",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 202,
          "quote": "- 정책 내용: 고객은 배송지마다 배달 방식 하나를 필수로 선택하고 공동현관 비밀번호는 필요한 경우에만 문자열로 입력한다. 기본 주소와 우편번호는 필수이며, 상세 주소는 선택 입력이다. **현재 MVP에서는 기본 주소 문자열에 `대구`가 포함된 경우에만 배송 가능으로 판단**한다. `대구`가 포함되지 않으면 배송지를 등록·수정할 수 없다. 주문을 생성할 때 해당 배송지의 배달 요청사항을 주문 데이터에 복사한다. 대구 단일 지역 MVP에서는 별도 지역 코드를 사용하지 않으며, 행정구역·좌표·우편번호를 이용한 정확한 지역 판정은 현재 범위에 포함하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q167",
  "group": "G084",
  "question": "서울 주소를 배송지로 등록할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.380099998656078,
  "retrievalMs": 2.7331999990565237,
  "hits": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8587943911552429,
      "score": 0.8587943911552429
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8344446420669556,
      "score": 0.8344446420669556
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8317159414291382,
      "score": 0.8317159414291382
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8301734328269958,
      "score": 0.8301734328269958
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8286305069923401,
      "score": 0.8286305069923401
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8587943911552429,
      "score": 0.8587943911552429
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8344446420669556,
      "score": 0.8344446420669556
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.8317159414291382,
      "score": 0.8317159414291382
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8301734328269958,
      "score": 0.8301734328269958
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8286305069923401,
      "score": 0.8286305069923401
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
        "denseScore": 0.8587943911552429,
        "score": 0.8587943911552429
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8344446420669556,
        "score": 0.8344446420669556
      },
      {
        "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
        "denseScore": 0.8317159414291382,
        "score": 0.8317159414291382
      },
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8301734328269958,
        "score": 0.8301734328269958
      },
      {
        "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
        "denseScore": 0.8286305069923401,
        "score": 0.8286305069923401
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1202,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ADDRESS-001",
        "anchor": "대구",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "originHit": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "originHit": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb"
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "originHit": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f"
    }
  ]
}
```

## Q168

기본 주소에 대구가 없는 부산 주소도 등록 가능한가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ADDRESS-001",
      "anchor": "대구",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 202,
          "quote": "- 정책 내용: 고객은 배송지마다 배달 방식 하나를 필수로 선택하고 공동현관 비밀번호는 필요한 경우에만 문자열로 입력한다. 기본 주소와 우편번호는 필수이며, 상세 주소는 선택 입력이다. **현재 MVP에서는 기본 주소 문자열에 `대구`가 포함된 경우에만 배송 가능으로 판단**한다. `대구`가 포함되지 않으면 배송지를 등록·수정할 수 없다. 주문을 생성할 때 해당 배송지의 배달 요청사항을 주문 데이터에 복사한다. 대구 단일 지역 MVP에서는 별도 지역 코드를 사용하지 않으며, 행정구역·좌표·우편번호를 이용한 정확한 지역 판정은 현재 범위에 포함하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q168",
  "group": "G084",
  "question": "기본 주소에 대구가 없는 부산 주소도 등록 가능한가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.746100000687875,
  "retrievalMs": 2.298399998835521,
  "hits": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8717980980873108,
      "score": 0.8717980980873108
    },
    {
      "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
      "denseScore": 0.8278623819351196,
      "score": 0.8278623819351196
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8254319429397583,
      "score": 0.8254319429397583
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8202124834060669,
      "score": 0.8202124834060669
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8202059864997864,
      "score": 0.8202059864997864
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8717980980873108,
      "score": 0.8717980980873108
    },
    {
      "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
      "denseScore": 0.8278623819351196,
      "score": 0.8278623819351196
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8254319429397583,
      "score": 0.8254319429397583
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "denseScore": 0.8202124834060669,
      "score": 0.8202124834060669
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8202059864997864,
      "score": 0.8202059864997864
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
        "denseScore": 0.8717980980873108,
        "score": 0.8717980980873108
      },
      {
        "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
        "denseScore": 0.8278623819351196,
        "score": 0.8278623819351196
      },
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8254319429397583,
        "score": 0.8254319429397583
      },
      {
        "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
        "denseScore": 0.8202124834060669,
        "score": 0.8202124834060669
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8202059864997864,
        "score": 0.8202059864997864
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 659,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ADDRESS-001",
        "anchor": "대구",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "originHit": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5"
    },
    {
      "chunkId": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6",
      "originHit": "knowledge-6-56b1a234e401d8023abfe6b204b90cdb1129b9ffcbc291b295b8e8f75739a2b6"
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    },
    {
      "chunkId": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9",
      "originHit": "knowledge-3-c1fecb9e32b5a6b0b9bf4a9edc8231db9247b608a60c148d4cd2765b40cba8c9"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    }
  ]
}
```

## Q183

점심 배송이 13시 00분 59초에 완료되면 지연인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "DLV-POL-DELAY-001",
      "anchor": "13:00:59",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 770,
          "quote": "- 점심 `13:00:59`, 저녁 `19:00:59`까지 완료하면 정상이고 그 이후 완료하면 지연이다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q183",
  "group": "G092",
  "question": "점심 배송이 13시 00분 59초에 완료되면 지연인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.679600000206847,
  "retrievalMs": 2.9095999998389743,
  "hits": [
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "denseScore": 0.893070638179779,
      "score": 0.893070638179779
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8758366703987122,
      "score": 0.8758366703987122
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8702996373176575,
      "score": 0.8702996373176575
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8656653165817261,
      "score": 0.8656653165817261
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8614099621772766,
      "score": 0.8614099621772766
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "denseScore": 0.893070638179779,
      "score": 0.893070638179779
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8758366703987122,
      "score": 0.8758366703987122
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8702996373176575,
      "score": 0.8702996373176575
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8656653165817261,
      "score": 0.8656653165817261
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8614099621772766,
      "score": 0.8614099621772766
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
        "denseScore": 0.893070638179779,
        "score": 0.893070638179779
      },
      {
        "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
        "denseScore": 0.8758366703987122,
        "score": 0.8758366703987122
      },
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.8702996373176575,
        "score": 0.8702996373176575
      },
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8656653165817261,
        "score": 0.8656653165817261
      },
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8614099621772766,
        "score": 0.8614099621772766
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1461,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "DLV-POL-DELAY-001",
        "anchor": "13:00:59",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "originHit": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5"
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "originHit": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38"
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    }
  ]
}
```

## Q184

오후 한 시가 지나 59초 안에 도착한 점심은 지연 처리되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "DLV-POL-DELAY-001",
      "anchor": "13:00:59",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 770,
          "quote": "- 점심 `13:00:59`, 저녁 `19:00:59`까지 완료하면 정상이고 그 이후 완료하면 지연이다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q184",
  "group": "G092",
  "question": "오후 한 시가 지나 59초 안에 도착한 점심은 지연 처리되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.861700000736164,
  "retrievalMs": 2.5557999997545267,
  "hits": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8537636995315552,
      "score": 0.8537636995315552
    },
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "denseScore": 0.8526057004928589,
      "score": 0.8526057004928589
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8442323207855225,
      "score": 0.8442323207855225
    },
    {
      "chunkId": "knowledge-1-ac1ba6aabd1a9612a9ef7ebd1989e3511eec07ea246bb5933de114aa8007335d",
      "denseScore": 0.8389002084732056,
      "score": 0.8389002084732056
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8356142044067383,
      "score": 0.8356142044067383
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8537636995315552,
      "score": 0.8537636995315552
    },
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "denseScore": 0.8526057004928589,
      "score": 0.8526057004928589
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8442323207855225,
      "score": 0.8442323207855225
    },
    {
      "chunkId": "knowledge-1-ac1ba6aabd1a9612a9ef7ebd1989e3511eec07ea246bb5933de114aa8007335d",
      "denseScore": 0.8389002084732056,
      "score": 0.8389002084732056
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8356142044067383,
      "score": 0.8356142044067383
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8537636995315552,
        "score": 0.8537636995315552
      },
      {
        "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
        "denseScore": 0.8526057004928589,
        "score": 0.8526057004928589
      },
      {
        "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
        "denseScore": 0.8442323207855225,
        "score": 0.8442323207855225
      },
      {
        "chunkId": "knowledge-1-ac1ba6aabd1a9612a9ef7ebd1989e3511eec07ea246bb5933de114aa8007335d",
        "denseScore": 0.8389002084732056,
        "score": 0.8389002084732056
      },
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8356142044067383,
        "score": 0.8356142044067383
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1173,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "DLV-POL-DELAY-001",
        "anchor": "13:00:59",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5",
      "originHit": "knowledge-5-bfe0bdac9d2cf048c6712f464acd068ff89c8062b4259a8b229d892afda7def5"
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "originHit": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38"
    },
    {
      "chunkId": "knowledge-1-ac1ba6aabd1a9612a9ef7ebd1989e3511eec07ea246bb5933de114aa8007335d",
      "originHit": "knowledge-1-ac1ba6aabd1a9612a9ef7ebd1989e3511eec07ea246bb5933de114aa8007335d"
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    }
  ]
}
```

## Q187

배송 실패 상세 화면에서 내부 실패 코드를 보여 주나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "DLV-POL-VIEW-001",
      "anchor": "실패 코드별로 세분화하지 않고",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 827,
          "quote": "Delivery-Service의 고객 조회에서 `FAILED` 상세 안내는 실패 코드별로 세분화하지 않고 `배송을 완료하지 못했습니다. 해당 배송 회차는 환불 대상입니다.` 한 문구만 사용한다. 내부 `failure_code`와 기사·관리자 메모는 고객에게 공개하지 않는다. Customer-Service가 소유하는 알림 템플릿·앱 내 알림 문구는 이 조회 문구와 별도 계약이며 Delivery-Service가 변경하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q187",
  "group": "G094",
  "question": "배송 실패 상세 화면에서 내부 실패 코드를 보여 주나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.748199998488417,
  "retrievalMs": 3.4851000000344357,
  "hits": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.906336784362793,
      "score": 0.906336784362793
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8805704712867737,
      "score": 0.8805704712867737
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.8760251402854919,
      "score": 0.8760251402854919
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8742021322250366,
      "score": 0.8742021322250366
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.8692873120307922,
      "score": 0.8692873120307922
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.906336784362793,
      "score": 0.906336784362793
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8805704712867737,
      "score": 0.8805704712867737
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.8760251402854919,
      "score": 0.8760251402854919
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8742021322250366,
      "score": 0.8742021322250366
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.8692873120307922,
      "score": 0.8692873120307922
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.906336784362793,
        "score": 0.906336784362793
      },
      {
        "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
        "denseScore": 0.8805704712867737,
        "score": 0.8805704712867737
      },
      {
        "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
        "denseScore": 0.8760251402854919,
        "score": 0.8760251402854919
      },
      {
        "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
        "denseScore": 0.8742021322250366,
        "score": 0.8742021322250366
      },
      {
        "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
        "denseScore": 0.8692873120307922,
        "score": 0.8692873120307922
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1771,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "DLV-POL-VIEW-001",
        "anchor": "실패 코드별로 세분화하지 않고",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "originHit": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286"
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "originHit": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853"
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "originHit": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38"
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "originHit": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380"
    }
  ]
}
```

## Q188

고객은 실패 사유 코드별로 다른 내부 안내를 보게 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "DLV-POL-VIEW-001",
      "anchor": "실패 코드별로 세분화하지 않고",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 827,
          "quote": "Delivery-Service의 고객 조회에서 `FAILED` 상세 안내는 실패 코드별로 세분화하지 않고 `배송을 완료하지 못했습니다. 해당 배송 회차는 환불 대상입니다.` 한 문구만 사용한다. 내부 `failure_code`와 기사·관리자 메모는 고객에게 공개하지 않는다. Customer-Service가 소유하는 알림 템플릿·앱 내 알림 문구는 이 조회 문구와 별도 계약이며 Delivery-Service가 변경하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q188",
  "group": "G094",
  "question": "고객은 실패 사유 코드별로 다른 내부 안내를 보게 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.787200000777375,
  "retrievalMs": 2.790100001220708,
  "hits": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8796970844268799,
      "score": 0.8796970844268799
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.8628743290901184,
      "score": 0.8628743290901184
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.857117772102356,
      "score": 0.857117772102356
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8546555638313293,
      "score": 0.8546555638313293
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8536486029624939,
      "score": 0.8536486029624939
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8796970844268799,
      "score": 0.8796970844268799
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.8628743290901184,
      "score": 0.8628743290901184
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "denseScore": 0.857117772102356,
      "score": 0.857117772102356
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8546555638313293,
      "score": 0.8546555638313293
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8536486029624939,
      "score": 0.8536486029624939
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8796970844268799,
        "score": 0.8796970844268799
      },
      {
        "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
        "denseScore": 0.8628743290901184,
        "score": 0.8628743290901184
      },
      {
        "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
        "denseScore": 0.857117772102356,
        "score": 0.857117772102356
      },
      {
        "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
        "denseScore": 0.8546555638313293,
        "score": 0.8546555638313293
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8536486029624939,
        "score": 0.8536486029624939
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1322,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "DLV-POL-VIEW-001",
        "anchor": "실패 코드별로 세분화하지 않고",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "originHit": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853"
    },
    {
      "chunkId": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746",
      "originHit": "knowledge-4-45b618c6e67b5946a5788626e464ad7118511b680c19f446e57eec23c277f746"
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "originHit": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    }
  ]
}
```

## Q201

첫 할인은 도시락 여러 개와 배송비 모두에 적용되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-002",
      "anchor": "3,000",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 637,
          "quote": "- 정책 내용: 실제 배송이 예정된 주문 한 건마다 배송비 3,000원을 부과한다. 주문이 생성되지 않은 날짜에는 배송비도 부과하지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 641,
          "quote": "한 이용 기간에 주문이 11건 생성되면 배송비는 `3,000원 × 11건 = 33,000원`이다."
        }
      ]
    },
    {
      "policyId": "POL-PAYMENT-009",
      "anchor": "나머지 도시락",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 796,
          "quote": "- 정책 내용: 고객의 첫 구독 결제에서 각 주문의 도시락 한 개에 해당하는 비용의 30%를 한 번 할인한다. 배송비와 각 주문의 나머지 도시락에는 할인을 적용하지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 802,
          "quote": "- 요일별 인원수가 달라도 각 주문에서 도시락 한 개까지만 30% 할인을 적용하고, 나머지 도시락은 정가로 계산한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q201",
  "group": "G101",
  "question": "첫 할인은 도시락 여러 개와 배송비 모두에 적용되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.5046999999322,
  "retrievalMs": 2.233499999420019,
  "hits": [
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "denseScore": 0.9139837622642517,
      "score": 0.9139837622642517
    },
    {
      "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
      "denseScore": 0.9097853899002075,
      "score": 0.9097853899002075
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.9067977070808411,
      "score": 0.9067977070808411
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "denseScore": 0.900127649307251,
      "score": 0.900127649307251
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8970811367034912,
      "score": 0.8970811367034912
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "denseScore": 0.9139837622642517,
      "score": 0.9139837622642517
    },
    {
      "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
      "denseScore": 0.9097853899002075,
      "score": 0.9097853899002075
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.9067977070808411,
      "score": 0.9067977070808411
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "denseScore": 0.900127649307251,
      "score": 0.900127649307251
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8970811367034912,
      "score": 0.8970811367034912
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
        "denseScore": 0.9139837622642517,
        "score": 0.9139837622642517
      },
      {
        "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
        "denseScore": 0.9097853899002075,
        "score": 0.9097853899002075
      },
      {
        "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
        "denseScore": 0.9067977070808411,
        "score": 0.9067977070808411
      },
      {
        "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
        "denseScore": 0.900127649307251,
        "score": 0.900127649307251
      },
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8970811367034912,
        "score": 0.8970811367034912
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 630,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-002",
        "anchor": "3,000",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-PAYMENT-009",
        "anchor": "나머지 도시락",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "originHit": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932"
    },
    {
      "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
      "originHit": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678"
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "originHit": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23"
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "originHit": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760"
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    }
  ]
}
```

## Q202

배송료와 추가 인분까지 첫 구독 30% 할인 대상인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-002",
      "anchor": "3,000",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 637,
          "quote": "- 정책 내용: 실제 배송이 예정된 주문 한 건마다 배송비 3,000원을 부과한다. 주문이 생성되지 않은 날짜에는 배송비도 부과하지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 641,
          "quote": "한 이용 기간에 주문이 11건 생성되면 배송비는 `3,000원 × 11건 = 33,000원`이다."
        }
      ]
    },
    {
      "policyId": "POL-PAYMENT-009",
      "anchor": "나머지 도시락",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 796,
          "quote": "- 정책 내용: 고객의 첫 구독 결제에서 각 주문의 도시락 한 개에 해당하는 비용의 30%를 한 번 할인한다. 배송비와 각 주문의 나머지 도시락에는 할인을 적용하지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 802,
          "quote": "- 요일별 인원수가 달라도 각 주문에서 도시락 한 개까지만 30% 할인을 적용하고, 나머지 도시락은 정가로 계산한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q202",
  "group": "G101",
  "question": "배송료와 추가 인분까지 첫 구독 30% 할인 대상인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.2965999996959,
  "retrievalMs": 2.600499999971362,
  "hits": [
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "denseScore": 0.8808156847953796,
      "score": 0.8808156847953796
    },
    {
      "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
      "denseScore": 0.8773772716522217,
      "score": 0.8773772716522217
    },
    {
      "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
      "denseScore": 0.8769526481628418,
      "score": 0.8769526481628418
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8748523592948914,
      "score": 0.8748523592948914
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8737406134605408,
      "score": 0.8737406134605408
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "denseScore": 0.8808156847953796,
      "score": 0.8808156847953796
    },
    {
      "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
      "denseScore": 0.8773772716522217,
      "score": 0.8773772716522217
    },
    {
      "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
      "denseScore": 0.8769526481628418,
      "score": 0.8769526481628418
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8748523592948914,
      "score": 0.8748523592948914
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8737406134605408,
      "score": 0.8737406134605408
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
        "denseScore": 0.8808156847953796,
        "score": 0.8808156847953796
      },
      {
        "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
        "denseScore": 0.8773772716522217,
        "score": 0.8773772716522217
      },
      {
        "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
        "denseScore": 0.8769526481628418,
        "score": 0.8769526481628418
      },
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8748523592948914,
        "score": 0.8748523592948914
      },
      {
        "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
        "denseScore": 0.8737406134605408,
        "score": 0.8737406134605408
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 748,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-002",
        "anchor": "3,000",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-PAYMENT-009",
        "anchor": "나머지 도시락",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 1,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932",
      "originHit": "knowledge-4-88ce0581d9b3f75d34803bc2d730e7a3a6e324d1590ba59ccd124f0e93fe5932"
    },
    {
      "chunkId": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678",
      "originHit": "knowledge-4-dfa4acacfd269ed53bfd9d79a918b30573ddd0c16b70748a5af19de3e88f9678"
    },
    {
      "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
      "originHit": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec"
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "originHit": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23"
    }
  ]
}
```

## Q203

구독을 해지하면 곧바로 회원 탈퇴도 가능한가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-003",
      "anchor": "자동 갱신을 중단",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 309,
          "quote": "- 정책 내용: 고객이 이용 중인 구독을 해지하면 자동 갱신을 중단한다. 이미 결제되어 이용 중인 현재 이용 기간은 즉시 종료하거나 환불하지 않고 마지막 날까지 유지한다. 결제 성공한 시작 예정 이용 기간은 시작일 전날 14:00 KST 전까지만 전액 취소할 수 있다."
        }
      ]
    },
    {
      "policyId": "POL-SUBSCRIPTION-015",
      "anchor": "실제 이용 기간이 종료되기 전",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 594,
          "quote": "- `해지 예정`은 다음 자동 갱신을 중단했을 뿐 현재 이용 기간이 끝난 상태가 아니다. 따라서 고객은 구독 해지를 신청했더라도 실제 이용 기간이 종료되기 전에는 회원 탈퇴할 수 없다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q203",
  "group": "G102",
  "question": "구독을 해지하면 곧바로 회원 탈퇴도 가능한가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.155499998494633,
  "retrievalMs": 2.1849999993719393,
  "hits": [
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.9057649374008179,
      "score": 0.9057649374008179
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.9040207266807556,
      "score": 0.9040207266807556
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8848398923873901,
      "score": 0.8848398923873901
    },
    {
      "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
      "denseScore": 0.8809832334518433,
      "score": 0.8809832334518433
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8798299431800842,
      "score": 0.8798299431800842
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.9057649374008179,
      "score": 0.9057649374008179
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.9040207266807556,
      "score": 0.9040207266807556
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8848398923873901,
      "score": 0.8848398923873901
    },
    {
      "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
      "denseScore": 0.8809832334518433,
      "score": 0.8809832334518433
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8798299431800842,
      "score": 0.8798299431800842
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
        "denseScore": 0.9057649374008179,
        "score": 0.9057649374008179
      },
      {
        "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
        "denseScore": 0.9040207266807556,
        "score": 0.9040207266807556
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8848398923873901,
        "score": 0.8848398923873901
      },
      {
        "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
        "denseScore": 0.8809832334518433,
        "score": 0.8809832334518433
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8798299431800842,
        "score": 0.8798299431800842
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 765,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-003",
        "anchor": "자동 갱신을 중단",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-SUBSCRIPTION-015",
        "anchor": "실제 이용 기간이 종료되기 전",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 0,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "originHit": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba"
    },
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "originHit": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda",
      "originHit": "knowledge-2-b20eb50e1c41af1da404a8063c299125a9fc2ddbede9b6ce8ca377f336ba3dda"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    }
  ]
}
```

## Q204

해지 신청과 계정 탈퇴를 동시에 완료할 수 있나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-003",
      "anchor": "자동 갱신을 중단",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 309,
          "quote": "- 정책 내용: 고객이 이용 중인 구독을 해지하면 자동 갱신을 중단한다. 이미 결제되어 이용 중인 현재 이용 기간은 즉시 종료하거나 환불하지 않고 마지막 날까지 유지한다. 결제 성공한 시작 예정 이용 기간은 시작일 전날 14:00 KST 전까지만 전액 취소할 수 있다."
        }
      ]
    },
    {
      "policyId": "POL-SUBSCRIPTION-015",
      "anchor": "실제 이용 기간이 종료되기 전",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 594,
          "quote": "- `해지 예정`은 다음 자동 갱신을 중단했을 뿐 현재 이용 기간이 끝난 상태가 아니다. 따라서 고객은 구독 해지를 신청했더라도 실제 이용 기간이 종료되기 전에는 회원 탈퇴할 수 없다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q204",
  "group": "G102",
  "question": "해지 신청과 계정 탈퇴를 동시에 완료할 수 있나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.726199998724042,
  "retrievalMs": 2.275700000609504,
  "hits": [
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.869563639163971,
      "score": 0.869563639163971
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8667716979980469,
      "score": 0.8667716979980469
    },
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.8656335473060608,
      "score": 0.8656335473060608
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8572089076042175,
      "score": 0.8572089076042175
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8570651412010193,
      "score": 0.8570651412010193
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "denseScore": 0.869563639163971,
      "score": 0.869563639163971
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8667716979980469,
      "score": 0.8667716979980469
    },
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "denseScore": 0.8656335473060608,
      "score": 0.8656335473060608
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8572089076042175,
      "score": 0.8572089076042175
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "denseScore": 0.8570651412010193,
      "score": 0.8570651412010193
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
        "denseScore": 0.869563639163971,
        "score": 0.869563639163971
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8667716979980469,
        "score": 0.8667716979980469
      },
      {
        "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
        "denseScore": 0.8656335473060608,
        "score": 0.8656335473060608
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8572089076042175,
        "score": 0.8572089076042175
      },
      {
        "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
        "denseScore": 0.8570651412010193,
        "score": 0.8570651412010193
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 691,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-003",
        "anchor": "자동 갱신을 중단",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-SUBSCRIPTION-015",
        "anchor": "실제 이용 기간이 종료되기 전",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 1,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120",
      "originHit": "knowledge-2-a908f8145146c3dbd7aa358d79eeaeb5dc811a723fdc9292d70e21d322e5e120"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba",
      "originHit": "knowledge-2-1e4384cd5e867c741dce0c677946f48dcccdca4297358198f682f40b420a90ba"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    },
    {
      "chunkId": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132",
      "originHit": "knowledge-7-a43da909098ce28ef24b549baa4705fac343fc5c7aeb73e30d2c01d10f6b5132"
    }
  ]
}
```

## Q207

첫 적용 기준일이 휴일이면 구독 시작과 주문 생성은 어떻게 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-007",
      "anchor": "가장 빠른 실제 배송일",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 419,
          "quote": "- 정책 내용: 첫 이용 기간 시작일은 구독 신청의 처리 기준 시각으로 계산한 반영 기준일 이후 가능한 가장 빠른 실제 배송일로 정하고, 첫 결제 성공 시 시작 예정 상태로 확정한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 424,
          "quote": "- 반영 기준일부터 고객이 선택한 배송 요일을 확인하고, 일요일과 공휴일을 제외한 가장 빠른 실제 배송일을 찾는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 429,
          "quote": "- 가능한 가장 빠른 실제 배송일의 `00:00 KST`에 구독 상태를 `시작 예정`에서 `이용 중`으로 바꾸고 첫 28일 이용 기간을 시작한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 435,
          "quote": "- 배송 요일이 월요일·화요일·수요일인 고객의 신청을 2026년 8월 15일 토요일 13:00에 접수하면 다음 날 일요일을 월요일로 조정하여 반영 기준일은 8월 17일 월요일이다. 8월 17일은 대체공휴일이므로 가능한 가장 빠른 실제 배송일인 8월 18일 화요일을 첫 이용 기간 시작일로 미리 계산한다."
        }
      ]
    },
    {
      "policyId": "POL-ORDER-006",
      "anchor": "공휴일",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1040,
          "quote": "- 정책 내용: 일요일과 대한민국의 공식 공휴일·대체공휴일에는 주문을 생성하지 않는다. 해당 날짜의 주문을 다른 날짜로 옮기지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1045,
          "quote": "- 반영 기준일이나 변경 적용일이 공휴일이어도 그 날짜에는 주문과 배송이 없다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1046,
          "quote": "- 공휴일 때문에 주문이 제외되어도 고객이 선택한 배송 요일 설정은 바뀌지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1050,
          "quote": "고객이 월요일·수요일·금요일을 선택했고 수요일이 공휴일이면 그 주에는 월요일과 금요일 주문만 생성한다. 수요일 주문을 목요일 등에 대신 생성하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q207",
  "group": "G104",
  "question": "첫 적용 기준일이 휴일이면 구독 시작과 주문 생성은 어떻게 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 13.10390000071493,
  "retrievalMs": 2.085899999656249,
  "hits": [
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.9070013761520386,
      "score": 0.9070013761520386
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.9017032384872437,
      "score": 0.9017032384872437
    },
    {
      "chunkId": "knowledge-1-41d5b60c2b4091c17a5e359adc4744b02b97a47a27d62b9037173cd75c4817dd",
      "denseScore": 0.9009389877319336,
      "score": 0.9009389877319336
    },
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "denseScore": 0.9008753299713135,
      "score": 0.9008753299713135
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.9001273512840271,
      "score": 0.9001273512840271
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.9070013761520386,
      "score": 0.9070013761520386
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "denseScore": 0.9017032384872437,
      "score": 0.9017032384872437
    },
    {
      "chunkId": "knowledge-1-41d5b60c2b4091c17a5e359adc4744b02b97a47a27d62b9037173cd75c4817dd",
      "denseScore": 0.9009389877319336,
      "score": 0.9009389877319336
    },
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "denseScore": 0.9008753299713135,
      "score": 0.9008753299713135
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "denseScore": 0.9001273512840271,
      "score": 0.9001273512840271
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
        "denseScore": 0.9070013761520386,
        "score": 0.9070013761520386
      },
      {
        "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
        "denseScore": 0.9017032384872437,
        "score": 0.9017032384872437
      },
      {
        "chunkId": "knowledge-1-41d5b60c2b4091c17a5e359adc4744b02b97a47a27d62b9037173cd75c4817dd",
        "denseScore": 0.9009389877319336,
        "score": 0.9009389877319336
      },
      {
        "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
        "denseScore": 0.9008753299713135,
        "score": 0.9008753299713135
      },
      {
        "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
        "denseScore": 0.9001273512840271,
        "score": 0.9001273512840271
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 503,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-007",
        "anchor": "가장 빠른 실제 배송일",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      },
      {
        "policyId": "POL-ORDER-006",
        "anchor": "공휴일",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "originHit": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62"
    },
    {
      "chunkId": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd",
      "originHit": "knowledge-1-6f23213dc49d05181589f60f9f6e0b30beb566218f5e1ae0647dc9b3283d58cd"
    },
    {
      "chunkId": "knowledge-1-41d5b60c2b4091c17a5e359adc4744b02b97a47a27d62b9037173cd75c4817dd",
      "originHit": "knowledge-1-41d5b60c2b4091c17a5e359adc4744b02b97a47a27d62b9037173cd75c4817dd"
    },
    {
      "chunkId": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8",
      "originHit": "knowledge-1-6b813855cfe83ff4b5af234744bd51eb9dcd1290a04069aae0d2d9d373bdb2a8"
    },
    {
      "chunkId": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26",
      "originHit": "knowledge-1-88afcc79c2e9848f6240b56aa86b92b23a4d66620acd5400b8ac8845435a4e26"
    }
  ]
}
```

## Q208

공휴일이 첫 배송 기준 날짜인 경우 실제 시작 날짜와 배송 주문을 설명해 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-007",
      "anchor": "가장 빠른 실제 배송일",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 419,
          "quote": "- 정책 내용: 첫 이용 기간 시작일은 구독 신청의 처리 기준 시각으로 계산한 반영 기준일 이후 가능한 가장 빠른 실제 배송일로 정하고, 첫 결제 성공 시 시작 예정 상태로 확정한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 424,
          "quote": "- 반영 기준일부터 고객이 선택한 배송 요일을 확인하고, 일요일과 공휴일을 제외한 가장 빠른 실제 배송일을 찾는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 429,
          "quote": "- 가능한 가장 빠른 실제 배송일의 `00:00 KST`에 구독 상태를 `시작 예정`에서 `이용 중`으로 바꾸고 첫 28일 이용 기간을 시작한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 435,
          "quote": "- 배송 요일이 월요일·화요일·수요일인 고객의 신청을 2026년 8월 15일 토요일 13:00에 접수하면 다음 날 일요일을 월요일로 조정하여 반영 기준일은 8월 17일 월요일이다. 8월 17일은 대체공휴일이므로 가능한 가장 빠른 실제 배송일인 8월 18일 화요일을 첫 이용 기간 시작일로 미리 계산한다."
        }
      ]
    },
    {
      "policyId": "POL-ORDER-006",
      "anchor": "공휴일",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1040,
          "quote": "- 정책 내용: 일요일과 대한민국의 공식 공휴일·대체공휴일에는 주문을 생성하지 않는다. 해당 날짜의 주문을 다른 날짜로 옮기지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1045,
          "quote": "- 반영 기준일이나 변경 적용일이 공휴일이어도 그 날짜에는 주문과 배송이 없다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1046,
          "quote": "- 공휴일 때문에 주문이 제외되어도 고객이 선택한 배송 요일 설정은 바뀌지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1050,
          "quote": "고객이 월요일·수요일·금요일을 선택했고 수요일이 공휴일이면 그 주에는 월요일과 금요일 주문만 생성한다. 수요일 주문을 목요일 등에 대신 생성하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q208",
  "group": "G104",
  "question": "공휴일이 첫 배송 기준 날짜인 경우 실제 시작 날짜와 배송 주문을 설명해 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 14.585799999622395,
  "retrievalMs": 2.1735000009357464,
  "hits": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.9099743962287903,
      "score": 0.9099743962287903
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.9037957191467285,
      "score": 0.9037957191467285
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "denseScore": 0.9009703993797302,
      "score": 0.9009703993797302
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.9000609517097473,
      "score": 0.9000609517097473
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8980074524879456,
      "score": 0.8980074524879456
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "denseScore": 0.9099743962287903,
      "score": 0.9099743962287903
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "denseScore": 0.9037957191467285,
      "score": 0.9037957191467285
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "denseScore": 0.9009703993797302,
      "score": 0.9009703993797302
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.9000609517097473,
      "score": 0.9000609517097473
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8980074524879456,
      "score": 0.8980074524879456
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
        "denseScore": 0.9099743962287903,
        "score": 0.9099743962287903
      },
      {
        "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
        "denseScore": 0.9037957191467285,
        "score": 0.9037957191467285
      },
      {
        "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
        "denseScore": 0.9009703993797302,
        "score": 0.9009703993797302
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.9000609517097473,
        "score": 0.9000609517097473
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8980074524879456,
        "score": 0.8980074524879456
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 919,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-007",
        "anchor": "가장 빠른 실제 배송일",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      },
      {
        "policyId": "POL-ORDER-006",
        "anchor": "공휴일",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb",
      "originHit": "knowledge-1-9f18c95ee560e49a1a29abf5d65c52f1d24932fa34155b07e1351dcc949f4abb"
    },
    {
      "chunkId": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d",
      "originHit": "knowledge-1-fadab19ee2f7659e134ccfe43e835b46679f4af33367a1a1da238143eb879a2d"
    },
    {
      "chunkId": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6",
      "originHit": "knowledge-1-9082e734df8816141c797bc5c38a78d7e51faa7da68addf593cd2355d76fc2c6"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    }
  ]
}
```

## Q211

정기결제 실패 뒤 재시도 일정과 최종 실패 결과를 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-005",
      "anchor": "13:00",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 695,
          "quote": "- 정책 내용: 09:00 정기결제에 실패하면 고객에게 실패 사실을 알리고, 같은 날 `13:00 KST`에 한 번 다시 결제한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 699,
          "quote": "- 13:00 재시도에 성공하면 다음 이용 기간을 갱신하고 추가 재시도는 진행하지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 700,
          "quote": "- 13:00 재시도는 09:00에 만든 같은 결제 거래·다음 이용 기간·주문을 사용하며 이용 기간에 저장한 처리 기준 시각과 결제금액을 다시 계산하지 않는다. 재시도를 시작할 때 기존 거래를 `재시도 대기`에서 `처리 중`으로 바꾼다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 701,
          "quote": "- 09:00 결제가 실패한 뒤 고객이 13:00 전에 현재 결제수단을 변경하면 13:00 재시도에는 변경된 현재 결제수단을 사용한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 702,
          "quote": "- 09:00과 13:00의 각 결제 시도는 시도를 시작할 때 확정한 결제수단으로 끝낸다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 703,
          "quote": "- 고객이 13:00 전에 구독을 해지하면 재시도하지 않고 결제 거래를 `재시도 중단`으로 바꾼다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 708,
          "quote": "현재 이용 기간 마지막 날인 9월 6일 09:00 정기결제에 실패하면 고객에게 알림을 보내고, 같은 날 13:00에 한 번 다시 결제한다. 고객이 그사이에 현재 결제수단을 변경했다면 13:00에는 변경한 결제수단을 사용한다."
        }
      ]
    },
    {
      "policyId": "POL-PAYMENT-006",
      "anchor": "다음 이용 기간을 시작하지 않는다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 728,
          "quote": "- 다음 이용 기간을 시작하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q211",
  "group": "G106",
  "question": "정기결제 실패 뒤 재시도 일정과 최종 실패 결과를 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.46289999835426,
  "retrievalMs": 2.1569000000454253,
  "hits": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "denseScore": 0.9017050266265869,
      "score": 0.9017050266265869
    },
    {
      "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
      "denseScore": 0.8837723731994629,
      "score": 0.8837723731994629
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "denseScore": 0.8827298879623413,
      "score": 0.8827298879623413
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8822531700134277,
      "score": 0.8822531700134277
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8819657564163208,
      "score": 0.8819657564163208
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "denseScore": 0.9017050266265869,
      "score": 0.9017050266265869
    },
    {
      "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
      "denseScore": 0.8837723731994629,
      "score": 0.8837723731994629
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "denseScore": 0.8827298879623413,
      "score": 0.8827298879623413
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8822531700134277,
      "score": 0.8822531700134277
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8819657564163208,
      "score": 0.8819657564163208
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
        "denseScore": 0.9017050266265869,
        "score": 0.9017050266265869
      },
      {
        "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
        "denseScore": 0.8837723731994629,
        "score": 0.8837723731994629
      },
      {
        "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
        "denseScore": 0.8827298879623413,
        "score": 0.8827298879623413
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8822531700134277,
        "score": 0.8822531700134277
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8819657564163208,
        "score": 0.8819657564163208
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 897,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-005",
        "anchor": "13:00",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      },
      {
        "policyId": "POL-PAYMENT-006",
        "anchor": "다음 이용 기간을 시작하지 않는다",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "originHit": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164"
    },
    {
      "chunkId": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd",
      "originHit": "knowledge-3-ff138c5394fc1b3b5a15eaf5c6bfc65f94c64bd3b1609c46342fc35255d810fd"
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "originHit": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    }
  ]
}
```

## Q212

자동결제를 재시도하는 시간과 그것도 실패했을 때 다음 기간 처리가 궁금해요.

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-005",
      "anchor": "13:00",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 695,
          "quote": "- 정책 내용: 09:00 정기결제에 실패하면 고객에게 실패 사실을 알리고, 같은 날 `13:00 KST`에 한 번 다시 결제한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 699,
          "quote": "- 13:00 재시도에 성공하면 다음 이용 기간을 갱신하고 추가 재시도는 진행하지 않는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 700,
          "quote": "- 13:00 재시도는 09:00에 만든 같은 결제 거래·다음 이용 기간·주문을 사용하며 이용 기간에 저장한 처리 기준 시각과 결제금액을 다시 계산하지 않는다. 재시도를 시작할 때 기존 거래를 `재시도 대기`에서 `처리 중`으로 바꾼다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 701,
          "quote": "- 09:00 결제가 실패한 뒤 고객이 13:00 전에 현재 결제수단을 변경하면 13:00 재시도에는 변경된 현재 결제수단을 사용한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 702,
          "quote": "- 09:00과 13:00의 각 결제 시도는 시도를 시작할 때 확정한 결제수단으로 끝낸다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 703,
          "quote": "- 고객이 13:00 전에 구독을 해지하면 재시도하지 않고 결제 거래를 `재시도 중단`으로 바꾼다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 708,
          "quote": "현재 이용 기간 마지막 날인 9월 6일 09:00 정기결제에 실패하면 고객에게 알림을 보내고, 같은 날 13:00에 한 번 다시 결제한다. 고객이 그사이에 현재 결제수단을 변경했다면 13:00에는 변경한 결제수단을 사용한다."
        }
      ]
    },
    {
      "policyId": "POL-PAYMENT-006",
      "anchor": "다음 이용 기간을 시작하지 않는다",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 728,
          "quote": "- 다음 이용 기간을 시작하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q212",
  "group": "G106",
  "question": "자동결제를 재시도하는 시간과 그것도 실패했을 때 다음 기간 처리가 궁금해요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.250699999640347,
  "retrievalMs": 2.241399999547866,
  "hits": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "denseScore": 0.9050133228302002,
      "score": 0.9050133228302002
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8997325301170349,
      "score": 0.8997325301170349
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "denseScore": 0.897158682346344,
      "score": 0.897158682346344
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.894012987613678,
      "score": 0.894012987613678
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.8930729627609253,
      "score": 0.8930729627609253
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "denseScore": 0.9050133228302002,
      "score": 0.9050133228302002
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8997325301170349,
      "score": 0.8997325301170349
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "denseScore": 0.897158682346344,
      "score": 0.897158682346344
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "denseScore": 0.894012987613678,
      "score": 0.894012987613678
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "denseScore": 0.8930729627609253,
      "score": 0.8930729627609253
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
        "denseScore": 0.9050133228302002,
        "score": 0.9050133228302002
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8997325301170349,
        "score": 0.8997325301170349
      },
      {
        "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
        "denseScore": 0.897158682346344,
        "score": 0.897158682346344
      },
      {
        "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
        "denseScore": 0.894012987613678,
        "score": 0.894012987613678
      },
      {
        "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
        "denseScore": 0.8930729627609253,
        "score": 0.8930729627609253
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1099,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-005",
        "anchor": "13:00",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      },
      {
        "policyId": "POL-PAYMENT-006",
        "anchor": "다음 이용 기간을 시작하지 않는다",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164",
      "originHit": "knowledge-2-d4862a8bbf827fa87349c29c62ac171fcbd71bdac81417bff3f1ce846548f164"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    },
    {
      "chunkId": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004",
      "originHit": "knowledge-3-8f401e79ad01d1b98a0bb16e613695a28ec183ae83024f918b889fb180509004"
    },
    {
      "chunkId": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853",
      "originHit": "knowledge-3-73e6d9da3b190aeff22bb2bc071591389080684054af1621e018fe997ee81853"
    },
    {
      "chunkId": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7",
      "originHit": "knowledge-2-de6a54138f655d778f18e278fb293c1c292b17e08e4a463d7d1f471126f3d9c7"
    }
  ]
}
```

## Q213

할인받은 주문이 배송 환불 대상이면 할인 전 금액을 환불하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-009",
      "anchor": "할인 금액",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 801,
          "quote": "- 할인 금액은 `할인 대상 도시락 비용 × 30%`다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 803,
          "quote": "- 첫 구독 결제금액은 `전체 도시락 정가 합계 - 할인 금액 + 전체 배송비`다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 820,
          "quote": "가정식 플랜에서 월요일 1명·수요일 2명·금요일 3명으로 설정하고 각 요일에 주문이 4건씩 생성되면 전체 도시락은 24개다. 전체 도시락 정가는 `8,900원 × 24개 = 213,600원`이고, 주문 12건에서 한 개씩 적용되는 할인 대상 금액은 `8,900원 × 12건 = 106,800원`이다. 할인 금액은 `106,800원 × 30% = 32,040원`, 전체 배송비는 `3,000원 × 12건 = 36,000원`이므로 첫 구독 결제금액은 `213,600원 - 32,040원 + 36,000원 = 217,560원`이다."
        }
      ]
    },
    {
      "policyId": "POL-ORDER-008",
      "anchor": "실제 배분금액",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1103,
          "quote": "- 정책 내용: 환불 대상으로 확정된 배송 건은 구독 서비스가 `배송 건 환불`을 만들고, 그 배송 건과 연결된 주문 한 건의 실제 배분금액을 해당 주문에 배분된 하나 이상의 원 결제에서 환불한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1117,
          "quote": "- 주문에 저장된 결제 당시 실제 배분금액 전체를 환불한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1118,
          "quote": "- 실제 배분금액에는 해당 주문의 모든 도시락 금액과 배송비가 포함되고, 첫 구독 주문이면 그 주문에 적용된 할인금액을 차감한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1120,
          "quote": "- 첫 구독 주문 한 건의 실제 배분금액은 `결제 당시 도시락 단가 × 주문 수량 + 배송비 - 해당 주문 할인금액`이다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1121,
          "quote": "- 자동 갱신 주문 한 건의 실제 배분금액은 할인이 없다면 `결제 당시 도시락 단가 × 주문 수량 + 배송비`다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1126,
          "quote": "가정식 플랜의 첫 구독 주문이 도시락 2개, 배송비 3,000원이고 도시락 한 개에 30% 할인을 적용했다면 실제 배분금액은 `8,900원 × 2개 + 3,000원 - 2,670원 = 18,130원`이다. 해당 배송 건이 환불 대상으로 확정되면 현재 가격이나 인원수와 관계없이 18,130원을 원 결제에서 부분 취소한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q213",
  "group": "G107",
  "question": "할인받은 주문이 배송 환불 대상이면 할인 전 금액을 환불하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 13.154399999621091,
  "retrievalMs": 2.4407000000792323,
  "hits": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8765078783035278,
      "score": 0.8765078783035278
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8721392750740051,
      "score": 0.8721392750740051
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8698195219039917,
      "score": 0.8698195219039917
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8672108054161072,
      "score": 0.8672108054161072
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8608530759811401,
      "score": 0.8608530759811401
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8765078783035278,
      "score": 0.8765078783035278
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8721392750740051,
      "score": 0.8721392750740051
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8698195219039917,
      "score": 0.8698195219039917
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8672108054161072,
      "score": 0.8672108054161072
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "denseScore": 0.8608530759811401,
      "score": 0.8608530759811401
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8765078783035278,
        "score": 0.8765078783035278
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8721392750740051,
        "score": 0.8721392750740051
      },
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.8698195219039917,
        "score": 0.8698195219039917
      },
      {
        "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
        "denseScore": 0.8672108054161072,
        "score": 0.8672108054161072
      },
      {
        "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
        "denseScore": 0.8608530759811401,
        "score": 0.8608530759811401
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1139,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-009",
        "anchor": "할인 금액",
        "policyHit": false,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-ORDER-008",
        "anchor": "실제 배분금액",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": false,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 4,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "originHit": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c"
    },
    {
      "chunkId": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286",
      "originHit": "knowledge-5-c3f5bb923c8a8d5d8830b11905e5081dddd60b762f508ba496b13aa819848286"
    }
  ]
}
```

## Q214

첫 할인 적용 주문의 배송 건 환불 금액은 어떻게 정하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-PAYMENT-009",
      "anchor": "할인 금액",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 801,
          "quote": "- 할인 금액은 `할인 대상 도시락 비용 × 30%`다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 803,
          "quote": "- 첫 구독 결제금액은 `전체 도시락 정가 합계 - 할인 금액 + 전체 배송비`다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 820,
          "quote": "가정식 플랜에서 월요일 1명·수요일 2명·금요일 3명으로 설정하고 각 요일에 주문이 4건씩 생성되면 전체 도시락은 24개다. 전체 도시락 정가는 `8,900원 × 24개 = 213,600원`이고, 주문 12건에서 한 개씩 적용되는 할인 대상 금액은 `8,900원 × 12건 = 106,800원`이다. 할인 금액은 `106,800원 × 30% = 32,040원`, 전체 배송비는 `3,000원 × 12건 = 36,000원`이므로 첫 구독 결제금액은 `213,600원 - 32,040원 + 36,000원 = 217,560원`이다."
        }
      ]
    },
    {
      "policyId": "POL-ORDER-008",
      "anchor": "실제 배분금액",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1103,
          "quote": "- 정책 내용: 환불 대상으로 확정된 배송 건은 구독 서비스가 `배송 건 환불`을 만들고, 그 배송 건과 연결된 주문 한 건의 실제 배분금액을 해당 주문에 배분된 하나 이상의 원 결제에서 환불한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1117,
          "quote": "- 주문에 저장된 결제 당시 실제 배분금액 전체를 환불한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1118,
          "quote": "- 실제 배분금액에는 해당 주문의 모든 도시락 금액과 배송비가 포함되고, 첫 구독 주문이면 그 주문에 적용된 할인금액을 차감한다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1120,
          "quote": "- 첫 구독 주문 한 건의 실제 배분금액은 `결제 당시 도시락 단가 × 주문 수량 + 배송비 - 해당 주문 할인금액`이다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1121,
          "quote": "- 자동 갱신 주문 한 건의 실제 배분금액은 할인이 없다면 `결제 당시 도시락 단가 × 주문 수량 + 배송비`다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 1126,
          "quote": "가정식 플랜의 첫 구독 주문이 도시락 2개, 배송비 3,000원이고 도시락 한 개에 30% 할인을 적용했다면 실제 배분금액은 `8,900원 × 2개 + 3,000원 - 2,670원 = 18,130원`이다. 해당 배송 건이 환불 대상으로 확정되면 현재 가격이나 인원수와 관계없이 18,130원을 원 결제에서 부분 취소한다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q214",
  "group": "G107",
  "question": "첫 할인 적용 주문의 배송 건 환불 금액은 어떻게 정하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 13.382699999056058,
  "retrievalMs": 2.5366999998368556,
  "hits": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8936489820480347,
      "score": 0.8936489820480347
    },
    {
      "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
      "denseScore": 0.8779215812683105,
      "score": 0.8779215812683105
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8736864328384399,
      "score": 0.8736864328384399
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8713098764419556,
      "score": 0.8713098764419556
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8706997632980347,
      "score": 0.8706997632980347
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8936489820480347,
      "score": 0.8936489820480347
    },
    {
      "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
      "denseScore": 0.8779215812683105,
      "score": 0.8779215812683105
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8736864328384399,
      "score": 0.8736864328384399
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.8713098764419556,
      "score": 0.8713098764419556
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "denseScore": 0.8706997632980347,
      "score": 0.8706997632980347
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8936489820480347,
        "score": 0.8936489820480347
      },
      {
        "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
        "denseScore": 0.8779215812683105,
        "score": 0.8779215812683105
      },
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8736864328384399,
        "score": 0.8736864328384399
      },
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.8713098764419556,
        "score": 0.8713098764419556
      },
      {
        "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
        "denseScore": 0.8706997632980347,
        "score": 0.8706997632980347
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1209,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-PAYMENT-009",
        "anchor": "할인 금액",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-ORDER-008",
        "anchor": "실제 배분금액",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    },
    {
      "chunkId": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec",
      "originHit": "knowledge-4-ce697113cd2a9b89eb98db3207876d592f2e3b25629fe309aaec76f640b230ec"
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576",
      "originHit": "knowledge-4-965705eb978d5adaa3321eae47050a86284f68a7e35eabebb13aa280a763f576"
    }
  ]
}
```

## Q217

경비실 수령을 요청하려면 어떤 방식을 선택하고 무엇을 입력하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ADDRESS-001",
      "anchor": "OTHER",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 210,
          "quote": "| `OTHER` | 기타 |"
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 213,
          "quote": "- `OTHER(기타)`를 선택한 경우에만 고객이 직접 입력한 문자열을 필수로 받는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 215,
          "quote": "- 주문 데이터에는 고객이 선택한 배달 방식 문자열 코드를 담고, `OTHER`인 경우에만 고객 직접 입력 문자열도 함께 담는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 221,
          "quote": "- `OTHER`를 선택하고 `경비실에 맡겨주세요`라고 입력하면 주문에는 `OTHER`와 고객 직접 입력 문자열 `경비실에 맡겨주세요`가 함께 유지된다."
        }
      ]
    },
    {
      "policyId": "DLV-POL-COMPLETE-002",
      "anchor": "문 앞 외",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 589,
          "quote": "| `OTHER` | 경비실·무인택배함 등 고객이 직접 입력한 문 앞 외 비대면 보관 | 고객 보관 요청 원문, 실제 보관 장소와 완료 사진 필수 |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q217",
  "group": "G109",
  "question": "경비실 수령을 요청하려면 어떤 방식을 선택하고 무엇을 입력하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.554199998703552,
  "retrievalMs": 2.274000000397791,
  "hits": [
    {
      "chunkId": "knowledge-1-20036d469af3d1e06b0c972a49fb79b47560a5a08ae42c6aa77d3e599499474f",
      "denseScore": 0.8568025231361389,
      "score": 0.8568025231361389
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8559461832046509,
      "score": 0.8559461832046509
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8471527099609375,
      "score": 0.8471527099609375
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8446134328842163,
      "score": 0.8446134328842163
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.84036785364151,
      "score": 0.84036785364151
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-20036d469af3d1e06b0c972a49fb79b47560a5a08ae42c6aa77d3e599499474f",
      "denseScore": 0.8568025231361389,
      "score": 0.8568025231361389
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8559461832046509,
      "score": 0.8559461832046509
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8471527099609375,
      "score": 0.8471527099609375
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8446134328842163,
      "score": 0.8446134328842163
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.84036785364151,
      "score": 0.84036785364151
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-20036d469af3d1e06b0c972a49fb79b47560a5a08ae42c6aa77d3e599499474f",
        "denseScore": 0.8568025231361389,
        "score": 0.8568025231361389
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8559461832046509,
        "score": 0.8559461832046509
      },
      {
        "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
        "denseScore": 0.8471527099609375,
        "score": 0.8471527099609375
      },
      {
        "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
        "denseScore": 0.8446134328842163,
        "score": 0.8446134328842163
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.84036785364151,
        "score": 0.84036785364151
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1125,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ADDRESS-001",
        "anchor": "OTHER",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      },
      {
        "policyId": "DLV-POL-COMPLETE-002",
        "anchor": "문 앞 외",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-20036d469af3d1e06b0c972a49fb79b47560a5a08ae42c6aa77d3e599499474f",
      "originHit": "knowledge-1-20036d469af3d1e06b0c972a49fb79b47560a5a08ae42c6aa77d3e599499474f"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "originHit": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f"
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "originHit": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    }
  ]
}
```

## Q218

문 앞이 아닌 지정 장소 보관의 주소 설정과 실제 전달 방식은 무엇인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-ADDRESS-001",
      "anchor": "OTHER",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 210,
          "quote": "| `OTHER` | 기타 |"
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 213,
          "quote": "- `OTHER(기타)`를 선택한 경우에만 고객이 직접 입력한 문자열을 필수로 받는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 215,
          "quote": "- 주문 데이터에는 고객이 선택한 배달 방식 문자열 코드를 담고, `OTHER`인 경우에만 고객 직접 입력 문자열도 함께 담는다."
        },
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 221,
          "quote": "- `OTHER`를 선택하고 `경비실에 맡겨주세요`라고 입력하면 주문에는 `OTHER`와 고객 직접 입력 문자열 `경비실에 맡겨주세요`가 함께 유지된다."
        }
      ]
    },
    {
      "policyId": "DLV-POL-COMPLETE-002",
      "anchor": "문 앞 외",
      "sources": [
        {
          "source": "Delivery-Service/챱챱_배달_정책.md",
          "line": 589,
          "quote": "| `OTHER` | 경비실·무인택배함 등 고객이 직접 입력한 문 앞 외 비대면 보관 | 고객 보관 요청 원문, 실제 보관 장소와 완료 사진 필수 |"
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q218",
  "group": "G109",
  "question": "문 앞이 아닌 지정 장소 보관의 주소 설정과 실제 전달 방식은 무엇인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 14.123099999778788,
  "retrievalMs": 2.205599999797414,
  "hits": [
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8566975593566895,
      "score": 0.8566975593566895
    },
    {
      "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
      "denseScore": 0.8477810621261597,
      "score": 0.8477810621261597
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8448597192764282,
      "score": 0.8448597192764282
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8446767926216125,
      "score": 0.8446767926216125
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8378003835678101,
      "score": 0.8378003835678101
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8566975593566895,
      "score": 0.8566975593566895
    },
    {
      "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
      "denseScore": 0.8477810621261597,
      "score": 0.8477810621261597
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "denseScore": 0.8448597192764282,
      "score": 0.8448597192764282
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8446767926216125,
      "score": 0.8446767926216125
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "denseScore": 0.8378003835678101,
      "score": 0.8378003835678101
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
        "denseScore": 0.8566975593566895,
        "score": 0.8566975593566895
      },
      {
        "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
        "denseScore": 0.8477810621261597,
        "score": 0.8477810621261597
      },
      {
        "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
        "denseScore": 0.8448597192764282,
        "score": 0.8448597192764282
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8446767926216125,
        "score": 0.8446767926216125
      },
      {
        "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
        "denseScore": 0.8378003835678101,
        "score": 0.8378003835678101
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1098,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-ADDRESS-001",
        "anchor": "OTHER",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      },
      {
        "policyId": "DLV-POL-COMPLETE-002",
        "anchor": "문 앞 외",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": true,
    "allSourceClauses": true,
    "nonGoldContextChunks": 3,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "originHit": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9"
    },
    {
      "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
      "originHit": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830"
    },
    {
      "chunkId": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f",
      "originHit": "knowledge-5-f79f5b651ecad83bf6213265df401e849ce56975cde9f7ff7f8389eea1ac083f"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7",
      "originHit": "knowledge-5-adf27f428af4dc53d5c64c75fad1b236c4caf99952dcdaddff407b1de7e54de7"
    }
  ]
}
```

## Q235

종료 후 재신청하면 새 구독이 생기고 첫 할인도 다시 생기나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-014",
      "anchor": "기존 구독을 재사용",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 559,
          "quote": "- 정책 내용: 인증 서비스가 제공한 같은 고객 식별자를 기준으로 구독 관계는 고객당 하나만 유지한다. 첫 결제 실패·시작 취소·종료 후 다시 구독하더라도 기존 구독을 재사용하고, 현재 상태와 구독 상태 이력으로 전체 생명주기를 관리한다."
        }
      ]
    },
    {
      "policyId": "POL-PAYMENT-009",
      "anchor": "복구되지 않으며",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 815,
          "quote": "- 첫 구독 결제 성공 후 구독을 시작 취소·해지·종료하더라도 사용한 할인은 복구되지 않으며, 이후 다시 구독해도 적용하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q235",
  "group": "G118",
  "question": "종료 후 재신청하면 새 구독이 생기고 첫 할인도 다시 생기나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 13.014099999054451,
  "retrievalMs": 2.2137999985716306,
  "hits": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.897104799747467,
      "score": 0.897104799747467
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8959729671478271,
      "score": 0.8959729671478271
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "denseScore": 0.8874527215957642,
      "score": 0.8874527215957642
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8832207918167114,
      "score": 0.8832207918167114
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8830741047859192,
      "score": 0.8830741047859192
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.897104799747467,
      "score": 0.897104799747467
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8959729671478271,
      "score": 0.8959729671478271
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "denseScore": 0.8874527215957642,
      "score": 0.8874527215957642
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "denseScore": 0.8832207918167114,
      "score": 0.8832207918167114
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8830741047859192,
      "score": 0.8830741047859192
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.897104799747467,
        "score": 0.897104799747467
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8959729671478271,
        "score": 0.8959729671478271
      },
      {
        "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
        "denseScore": 0.8874527215957642,
        "score": 0.8874527215957642
      },
      {
        "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
        "denseScore": 0.8832207918167114,
        "score": 0.8832207918167114
      },
      {
        "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
        "denseScore": 0.8830741047859192,
        "score": 0.8830741047859192
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1132,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-014",
        "anchor": "기존 구독을 재사용",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-PAYMENT-009",
        "anchor": "복구되지 않으며",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4",
      "originHit": "knowledge-3-ccca7c30cf1342f1ff1eb44245c09b5b96f2c6841dc62e70611a19ea9c89adc4"
    },
    {
      "chunkId": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432",
      "originHit": "knowledge-3-c6bcc1a0da7d00c618684ef1094658a2fc3e90f09837fe1fcea535529ff07432"
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "originHit": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011"
    }
  ]
}
```

## Q236

구독 재신청 때 기존 관계와 할인 사용 이력은 어떻게 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "POLICY",
  "rationale": "발췌 원문에서 필수 근거를 회수해야 함",
  "gold": [
    {
      "policyId": "POL-SUBSCRIPTION-014",
      "anchor": "기존 구독을 재사용",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 559,
          "quote": "- 정책 내용: 인증 서비스가 제공한 같은 고객 식별자를 기준으로 구독 관계는 고객당 하나만 유지한다. 첫 결제 실패·시작 취소·종료 후 다시 구독하더라도 기존 구독을 재사용하고, 현재 상태와 구독 상태 이력으로 전체 생명주기를 관리한다."
        }
      ]
    },
    {
      "policyId": "POL-PAYMENT-009",
      "anchor": "복구되지 않으며",
      "sources": [
        {
          "source": "Subscription-Service/챱챱_구독_정책.md",
          "line": 815,
          "quote": "- 첫 구독 결제 성공 후 구독을 시작 취소·해지·종료하더라도 사용한 할인은 복구되지 않으며, 이후 다시 구독해도 적용하지 않는다."
        }
      ]
    }
  ]
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q236",
  "group": "G118",
  "question": "구독 재신청 때 기존 관계와 할인 사용 이력은 어떻게 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.316500000451924,
  "retrievalMs": 2.179499999328982,
  "hits": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8935250043869019,
      "score": 0.8935250043869019
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8871296644210815,
      "score": 0.8871296644210815
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "denseScore": 0.8776242733001709,
      "score": 0.8776242733001709
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8757327795028687,
      "score": 0.8757327795028687
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8751170635223389,
      "score": 0.8751170635223389
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8935250043869019,
      "score": 0.8935250043869019
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8871296644210815,
      "score": 0.8871296644210815
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "denseScore": 0.8776242733001709,
      "score": 0.8776242733001709
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "denseScore": 0.8757327795028687,
      "score": 0.8757327795028687
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "denseScore": 0.8751170635223389,
      "score": 0.8751170635223389
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8935250043869019,
        "score": 0.8935250043869019
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8871296644210815,
        "score": 0.8871296644210815
      },
      {
        "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
        "denseScore": 0.8776242733001709,
        "score": 0.8776242733001709
      },
      {
        "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
        "denseScore": 0.8757327795028687,
        "score": 0.8757327795028687
      },
      {
        "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
        "denseScore": 0.8751170635223389,
        "score": 0.8751170635223389
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 987,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": true,
    "checks": [
      {
        "policyId": "POL-SUBSCRIPTION-014",
        "anchor": "기존 구독을 재사용",
        "policyHit": true,
        "anchorHit": false,
        "sourceClauseHit": false
      },
      {
        "policyId": "POL-PAYMENT-009",
        "anchor": "복구되지 않으며",
        "policyHit": true,
        "anchorHit": true,
        "sourceClauseHit": true
      }
    ],
    "allPolicies": true,
    "allAnchors": false,
    "allSourceClauses": false,
    "nonGoldContextChunks": 2,
    "nonPolicyQuestionReturnedCandidates": null,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "originHit": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c"
    },
    {
      "chunkId": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c",
      "originHit": "knowledge-2-41bd9b8ece0ad270f6d58ec5097802fdaccfd1ad2df83c3806a3440a35b5122c"
    },
    {
      "chunkId": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011",
      "originHit": "knowledge-1-c17c7c1b57e52ee9ff6775af8b03256e9da70a2425aa26ec2246a9095d423011"
    }
  ]
}
```

## Q241

카드 취소 후 제 은행에 환불금이 정확히 몇 영업일 뒤 들어오나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "원문에 은행별 환불 입금 소요일 없음",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q241",
  "group": "G121",
  "question": "카드 취소 후 제 은행에 환불금이 정확히 몇 영업일 뒤 들어오나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 13.101999998980318,
  "retrievalMs": 2.4492999982612673,
  "hits": [
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.858196496963501,
      "score": 0.858196496963501
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8576726913452148,
      "score": 0.8576726913452148
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "denseScore": 0.8552185893058777,
      "score": 0.8552185893058777
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8544186353683472,
      "score": 0.8544186353683472
    },
    {
      "chunkId": "knowledge-4-73030eb14d25bdf94695b828e0aa9c2854437f2a9c5888509edda0728138b17b",
      "denseScore": 0.8516604900360107,
      "score": 0.8516604900360107
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "denseScore": 0.858196496963501,
      "score": 0.858196496963501
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "denseScore": 0.8576726913452148,
      "score": 0.8576726913452148
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "denseScore": 0.8552185893058777,
      "score": 0.8552185893058777
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8544186353683472,
      "score": 0.8544186353683472
    },
    {
      "chunkId": "knowledge-4-73030eb14d25bdf94695b828e0aa9c2854437f2a9c5888509edda0728138b17b",
      "denseScore": 0.8516604900360107,
      "score": 0.8516604900360107
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
        "denseScore": 0.858196496963501,
        "score": 0.858196496963501
      },
      {
        "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
        "denseScore": 0.8576726913452148,
        "score": 0.8576726913452148
      },
      {
        "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
        "denseScore": 0.8552185893058777,
        "score": 0.8552185893058777
      },
      {
        "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
        "denseScore": 0.8544186353683472,
        "score": 0.8544186353683472
      },
      {
        "chunkId": "knowledge-4-73030eb14d25bdf94695b828e0aa9c2854437f2a9c5888509edda0728138b17b",
        "denseScore": 0.8516604900360107,
        "score": 0.8516604900360107
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 862,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8",
      "originHit": "knowledge-2-6cffe507dec1e28068d9458d2d84f0fa0127b7a836448bb2e522d690e91a20d8"
    },
    {
      "chunkId": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8",
      "originHit": "knowledge-2-2a4ae7a2c566f3587bbe16e5f340bf8c5fff4b48536e432594002baea81362d8"
    },
    {
      "chunkId": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb",
      "originHit": "knowledge-3-5360b2941f9542417523db3076894956684308ead23bb93f9e00ccf50a2e2cfb"
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "originHit": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1"
    },
    {
      "chunkId": "knowledge-4-73030eb14d25bdf94695b828e0aa9c2854437f2a9c5888509edda0728138b17b",
      "originHit": "knowledge-4-73030eb14d25bdf94695b828e0aa9c2854437f2a9c5888509edda0728138b17b"
    }
  ]
}
```

## Q242

은행별 환불 입금 완료까지 걸리는 일수를 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "원문에 은행별 환불 입금 소요일 없음",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q242",
  "group": "G121",
  "question": "은행별 환불 입금 완료까지 걸리는 일수를 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.446099999579019,
  "retrievalMs": 2.5181999990309123,
  "hits": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8662562370300293,
      "score": 0.8662562370300293
    },
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "denseScore": 0.864172637462616,
      "score": 0.864172637462616
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8618994355201721,
      "score": 0.8618994355201721
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8616430759429932,
      "score": 0.8616430759429932
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8612256050109863,
      "score": 0.8612256050109863
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8662562370300293,
      "score": 0.8662562370300293
    },
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "denseScore": 0.864172637462616,
      "score": 0.864172637462616
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8618994355201721,
      "score": 0.8618994355201721
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8616430759429932,
      "score": 0.8616430759429932
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8612256050109863,
      "score": 0.8612256050109863
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8662562370300293,
        "score": 0.8662562370300293
      },
      {
        "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
        "denseScore": 0.864172637462616,
        "score": 0.864172637462616
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8618994355201721,
        "score": 0.8618994355201721
      },
      {
        "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
        "denseScore": 0.8616430759429932,
        "score": 0.8616430759429932
      },
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8612256050109863,
        "score": 0.8612256050109863
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1210,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818",
      "originHit": "knowledge-1-16752efa8b40edd99c0f8bb9285f8df1d30019422168bfcd3bd532278487a818"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "originHit": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1"
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    }
  ]
}
```

## Q247

배송된 도시락의 소비기한이 정확히 며칠인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "상품별 소비기한 원본 없음",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q247",
  "group": "G124",
  "question": "배송된 도시락의 소비기한이 정확히 며칠인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.983599999643047,
  "retrievalMs": 2.273599999170983,
  "hits": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8731705546379089,
      "score": 0.8731705546379089
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8680007457733154,
      "score": 0.8680007457733154
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8677600026130676,
      "score": 0.8677600026130676
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8652676343917847,
      "score": 0.8652676343917847
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "denseScore": 0.861518144607544,
      "score": 0.861518144607544
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8731705546379089,
      "score": 0.8731705546379089
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8680007457733154,
      "score": 0.8680007457733154
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "denseScore": 0.8677600026130676,
      "score": 0.8677600026130676
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8652676343917847,
      "score": 0.8652676343917847
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "denseScore": 0.861518144607544,
      "score": 0.861518144607544
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8731705546379089,
        "score": 0.8731705546379089
      },
      {
        "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
        "denseScore": 0.8680007457733154,
        "score": 0.8680007457733154
      },
      {
        "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
        "denseScore": 0.8677600026130676,
        "score": 0.8677600026130676
      },
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8652676343917847,
        "score": 0.8652676343917847
      },
      {
        "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
        "denseScore": 0.861518144607544,
        "score": 0.861518144607544
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1212,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "originHit": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1"
    },
    {
      "chunkId": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23",
      "originHit": "knowledge-4-8092cba49291a4be7cc1fc1a16a08ff41f8085f4bc326369a4e414008cdccb23"
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    },
    {
      "chunkId": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab",
      "originHit": "knowledge-1-2d7a0e02117051d35fdb2e371c27b46a3f4445885c9cc1e79d6c9b84f88134ab"
    }
  ]
}
```

## Q248

모든 메뉴에 적용되는 정확한 소비기한 날짜 수를 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "상품별 소비기한 원본 없음",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q248",
  "group": "G124",
  "question": "모든 메뉴에 적용되는 정확한 소비기한 날짜 수를 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.413500000548083,
  "retrievalMs": 2.4962999996205326,
  "hits": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8710283041000366,
      "score": 0.8710283041000366
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8689864873886108,
      "score": 0.8689864873886108
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "denseScore": 0.8677987456321716,
      "score": 0.8677987456321716
    },
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "denseScore": 0.8629764318466187,
      "score": 0.8629764318466187
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8623555302619934,
      "score": 0.8623555302619934
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8710283041000366,
      "score": 0.8710283041000366
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8689864873886108,
      "score": 0.8689864873886108
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "denseScore": 0.8677987456321716,
      "score": 0.8677987456321716
    },
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "denseScore": 0.8629764318466187,
      "score": 0.8629764318466187
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8623555302619934,
      "score": 0.8623555302619934
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8710283041000366,
        "score": 0.8710283041000366
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8689864873886108,
        "score": 0.8689864873886108
      },
      {
        "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
        "denseScore": 0.8677987456321716,
        "score": 0.8677987456321716
      },
      {
        "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
        "denseScore": 0.8629764318466187,
        "score": 0.8629764318466187
      },
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8623555302619934,
        "score": 0.8623555302619934
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1293,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233",
      "originHit": "knowledge-1-ea7e3a4d49a07bf043ea5d1ab9130bd64c5381b947f31dc89394ec6b6025b233"
    },
    {
      "chunkId": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1",
      "originHit": "knowledge-1-b3226acc1749d4d3f48d754adf3148447a94060ac35e91bd3de037865eb628d1"
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    }
  ]
}
```

## Q251

도시락 보관 온도를 정확히 몇 도로 맞춰야 하나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "제품별 보관 온도 미확정",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q251",
  "group": "G126",
  "question": "도시락 보관 온도를 정확히 몇 도로 맞춰야 하나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.919599999600905,
  "retrievalMs": 2.439899999444606,
  "hits": [
    {
      "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
      "denseScore": 0.8868923187255859,
      "score": 0.8868923187255859
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8619277477264404,
      "score": 0.8619277477264404
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8581773042678833,
      "score": 0.8581773042678833
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8488517999649048,
      "score": 0.8488517999649048
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "denseScore": 0.8424898386001587,
      "score": 0.8424898386001587
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
      "denseScore": 0.8868923187255859,
      "score": 0.8868923187255859
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8619277477264404,
      "score": 0.8619277477264404
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8581773042678833,
      "score": 0.8581773042678833
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.8488517999649048,
      "score": 0.8488517999649048
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "denseScore": 0.8424898386001587,
      "score": 0.8424898386001587
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
        "denseScore": 0.8868923187255859,
        "score": 0.8868923187255859
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8619277477264404,
        "score": 0.8619277477264404
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8581773042678833,
        "score": 0.8581773042678833
      },
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.8488517999649048,
        "score": 0.8488517999649048
      },
      {
        "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
        "denseScore": 0.8424898386001587,
        "score": 0.8424898386001587
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1099,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
      "originHit": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    },
    {
      "chunkId": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760",
      "originHit": "knowledge-3-ced8f0a58cf109ace1428202e0314ca433a61f7b20e08536716b35b3e1bee760"
    }
  ]
}
```

## Q252

모든 도시락에 공통인 안전 보관 온도 수치를 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "제품별 보관 온도 미확정",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q252",
  "group": "G126",
  "question": "모든 도시락에 공통인 안전 보관 온도 수치를 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.991999999736436,
  "retrievalMs": 2.3172000001068227,
  "hits": [
    {
      "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
      "denseScore": 0.8861358165740967,
      "score": 0.8861358165740967
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8825607299804688,
      "score": 0.8825607299804688
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8717323541641235,
      "score": 0.8717323541641235
    },
    {
      "chunkId": "knowledge-5-c28f3bcef1b2ba6034bb161f544ffaf4e58da98e5437c6bc2bb5b73494b94659",
      "denseScore": 0.8651261329650879,
      "score": 0.8651261329650879
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.858557939529419,
      "score": 0.858557939529419
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
      "denseScore": 0.8861358165740967,
      "score": 0.8861358165740967
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8825607299804688,
      "score": 0.8825607299804688
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8717323541641235,
      "score": 0.8717323541641235
    },
    {
      "chunkId": "knowledge-5-c28f3bcef1b2ba6034bb161f544ffaf4e58da98e5437c6bc2bb5b73494b94659",
      "denseScore": 0.8651261329650879,
      "score": 0.8651261329650879
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "denseScore": 0.858557939529419,
      "score": 0.858557939529419
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
        "denseScore": 0.8861358165740967,
        "score": 0.8861358165740967
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8825607299804688,
        "score": 0.8825607299804688
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8717323541641235,
        "score": 0.8717323541641235
      },
      {
        "chunkId": "knowledge-5-c28f3bcef1b2ba6034bb161f544ffaf4e58da98e5437c6bc2bb5b73494b94659",
        "denseScore": 0.8651261329650879,
        "score": 0.8651261329650879
      },
      {
        "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
        "denseScore": 0.858557939529419,
        "score": 0.858557939529419
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1296,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0",
      "originHit": "knowledge-5-4ed491b443a62df28a3ee5d4dcf918b43fe08c87fadac55ceaffe190b97cedb0"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-5-c28f3bcef1b2ba6034bb161f544ffaf4e58da98e5437c6bc2bb5b73494b94659",
      "originHit": "knowledge-5-c28f3bcef1b2ba6034bb161f544ffaf4e58da98e5437c6bc2bb5b73494b94659"
    },
    {
      "chunkId": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd",
      "originHit": "knowledge-4-9d6fcc3000053440317b07b08a1e32af103aa132672c7f0b210ef670c568c6cd"
    }
  ]
}
```

## Q265

지금 바꾸면 언제 적용돼요?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "어떤 설정과 요청 시각인지 정보 부족",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q265",
  "group": "G133",
  "question": "지금 바꾸면 언제 적용돼요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.976899999150191,
  "retrievalMs": 2.62750000001688,
  "hits": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8792403340339661,
      "score": 0.8792403340339661
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.8674539923667908,
      "score": 0.8674539923667908
    },
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "denseScore": 0.8607971668243408,
      "score": 0.8607971668243408
    },
    {
      "chunkId": "knowledge-2-75af1c2298b0ded505208242bcc05fd20e3f8f2bf8bc1b79c87acf0952ce182b",
      "denseScore": 0.860581636428833,
      "score": 0.860581636428833
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8572408556938171,
      "score": 0.8572408556938171
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8792403340339661,
      "score": 0.8792403340339661
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.8674539923667908,
      "score": 0.8674539923667908
    },
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "denseScore": 0.8607971668243408,
      "score": 0.8607971668243408
    },
    {
      "chunkId": "knowledge-2-75af1c2298b0ded505208242bcc05fd20e3f8f2bf8bc1b79c87acf0952ce182b",
      "denseScore": 0.860581636428833,
      "score": 0.860581636428833
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8572408556938171,
      "score": 0.8572408556938171
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8792403340339661,
        "score": 0.8792403340339661
      },
      {
        "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
        "denseScore": 0.8674539923667908,
        "score": 0.8674539923667908
      },
      {
        "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
        "denseScore": 0.8607971668243408,
        "score": 0.8607971668243408
      },
      {
        "chunkId": "knowledge-2-75af1c2298b0ded505208242bcc05fd20e3f8f2bf8bc1b79c87acf0952ce182b",
        "denseScore": 0.860581636428833,
        "score": 0.860581636428833
      },
      {
        "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
        "denseScore": 0.8572408556938171,
        "score": 0.8572408556938171
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1072,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "originHit": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738"
    },
    {
      "chunkId": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39",
      "originHit": "knowledge-2-6edd3ba9ff34f839c02d9adb963e6f5cb6f85a72949245716d2d5afa7a5e4d39"
    },
    {
      "chunkId": "knowledge-2-75af1c2298b0ded505208242bcc05fd20e3f8f2bf8bc1b79c87acf0952ce182b",
      "originHit": "knowledge-2-75af1c2298b0ded505208242bcc05fd20e3f8f2bf8bc1b79c87acf0952ce182b"
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "originHit": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0"
    }
  ]
}
```

## Q266

변경하면 내일부터 되나요?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "어떤 설정과 요청 시각인지 정보 부족",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q266",
  "group": "G133",
  "question": "변경하면 내일부터 되나요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.866499998883228,
  "retrievalMs": 2.8244000004633563,
  "hits": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8844948410987854,
      "score": 0.8844948410987854
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.870384693145752,
      "score": 0.870384693145752
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8662130832672119,
      "score": 0.8662130832672119
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.865805983543396,
      "score": 0.865805983543396
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8618435263633728,
      "score": 0.8618435263633728
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8844948410987854,
      "score": 0.8844948410987854
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "denseScore": 0.870384693145752,
      "score": 0.870384693145752
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "denseScore": 0.8662130832672119,
      "score": 0.8662130832672119
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "denseScore": 0.865805983543396,
      "score": 0.865805983543396
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8618435263633728,
      "score": 0.8618435263633728
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8844948410987854,
        "score": 0.8844948410987854
      },
      {
        "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
        "denseScore": 0.870384693145752,
        "score": 0.870384693145752
      },
      {
        "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
        "denseScore": 0.8662130832672119,
        "score": 0.8662130832672119
      },
      {
        "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
        "denseScore": 0.865805983543396,
        "score": 0.865805983543396
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8618435263633728,
        "score": 0.8618435263633728
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1120,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    },
    {
      "chunkId": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738",
      "originHit": "knowledge-2-c57e084f68f36ca3c94724fb03703e9389c395d44aef51a472350e827fb07738"
    },
    {
      "chunkId": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0",
      "originHit": "knowledge-2-a9f41a7f8252f0dd0a8363275b24383a6a25acacc62fce65c2d4a75a687634b0"
    },
    {
      "chunkId": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62",
      "originHit": "knowledge-3-4c8d9eff9c126814e637efe68c888e3689fad32d431096d6364193fec9220d62"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    }
  ]
}
```

## Q269

집에 없는데 괜찮겠죠?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "배송 현장 조건이 없는 수령 판단",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q269",
  "group": "G135",
  "question": "집에 없는데 괜찮겠죠?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.645100000852835,
  "retrievalMs": 2.0042999985889765,
  "hits": [
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.840454638004303,
      "score": 0.840454638004303
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8314223885536194,
      "score": 0.8314223885536194
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8279830813407898,
      "score": 0.8279830813407898
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8278842568397522,
      "score": 0.8278842568397522
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8262908458709717,
      "score": 0.8262908458709717
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.840454638004303,
      "score": 0.840454638004303
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8314223885536194,
      "score": 0.8314223885536194
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "denseScore": 0.8279830813407898,
      "score": 0.8279830813407898
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8278842568397522,
      "score": 0.8278842568397522
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8262908458709717,
      "score": 0.8262908458709717
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
        "denseScore": 0.840454638004303,
        "score": 0.840454638004303
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8314223885536194,
        "score": 0.8314223885536194
      },
      {
        "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
        "denseScore": 0.8279830813407898,
        "score": 0.8279830813407898
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8278842568397522,
        "score": 0.8278842568397522
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8262908458709717,
        "score": 0.8262908458709717
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 792,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "originHit": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540",
      "originHit": "knowledge-2-04f4dea708e153cb848168a475b068a8cacfaa785fc5a570d006be2fce79a540"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    }
  ]
}
```

## Q270

부재 중이니까 알아서 안전하게 두겠죠?

### 기대 근거·처리

```json
{
  "expectedRoute": "INSUFFICIENT",
  "rationale": "배송 현장 조건이 없는 수령 판단",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q270",
  "group": "G135",
  "question": "부재 중이니까 알아서 안전하게 두겠죠?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.885499999654712,
  "retrievalMs": 2.5420000001759036,
  "hits": [
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8508859276771545,
      "score": 0.8508859276771545
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8470149636268616,
      "score": 0.8470149636268616
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8457863330841064,
      "score": 0.8457863330841064
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8379613161087036,
      "score": 0.8379613161087036
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8323819637298584,
      "score": 0.8323819637298584
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8508859276771545,
      "score": 0.8508859276771545
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8470149636268616,
      "score": 0.8470149636268616
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "denseScore": 0.8457863330841064,
      "score": 0.8457863330841064
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8379613161087036,
      "score": 0.8379613161087036
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8323819637298584,
      "score": 0.8323819637298584
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
        "denseScore": 0.8508859276771545,
        "score": 0.8508859276771545
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8470149636268616,
        "score": 0.8470149636268616
      },
      {
        "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
        "denseScore": 0.8457863330841064,
        "score": 0.8457863330841064
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8379613161087036,
        "score": 0.8379613161087036
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8323819637298584,
        "score": 0.8323819637298584
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1016,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "originHit": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec",
      "originHit": "knowledge-5-713b28c5788648d5b7dc0aab948a0534db7079f7d942496a25bb770ec3c194ec"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    }
  ]
}
```

## Q277

지금 제 구독이 이용 중인가요?

### 기대 근거·처리

```json
{
  "expectedRoute": "CURRENT_STATE",
  "rationale": "개인 구독 상태 조회 필요",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q277",
  "group": "G139",
  "question": "지금 제 구독이 이용 중인가요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 8.780899999692338,
  "retrievalMs": 2.171699999962584,
  "hits": [
    {
      "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
      "denseScore": 0.8786822557449341,
      "score": 0.8786822557449341
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "denseScore": 0.872813880443573,
      "score": 0.872813880443573
    },
    {
      "chunkId": "knowledge-3-f2288760b2100b5c59709aca8ba036fd87bf4d5aaddf8a644c04b56a5d8f7b60",
      "denseScore": 0.8669867515563965,
      "score": 0.8669867515563965
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "denseScore": 0.8668216466903687,
      "score": 0.8668216466903687
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8654289245605469,
      "score": 0.8654289245605469
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
      "denseScore": 0.8786822557449341,
      "score": 0.8786822557449341
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "denseScore": 0.872813880443573,
      "score": 0.872813880443573
    },
    {
      "chunkId": "knowledge-3-f2288760b2100b5c59709aca8ba036fd87bf4d5aaddf8a644c04b56a5d8f7b60",
      "denseScore": 0.8669867515563965,
      "score": 0.8669867515563965
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "denseScore": 0.8668216466903687,
      "score": 0.8668216466903687
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8654289245605469,
      "score": 0.8654289245605469
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
        "denseScore": 0.8786822557449341,
        "score": 0.8786822557449341
      },
      {
        "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
        "denseScore": 0.872813880443573,
        "score": 0.872813880443573
      },
      {
        "chunkId": "knowledge-3-f2288760b2100b5c59709aca8ba036fd87bf4d5aaddf8a644c04b56a5d8f7b60",
        "denseScore": 0.8669867515563965,
        "score": 0.8669867515563965
      },
      {
        "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
        "denseScore": 0.8668216466903687,
        "score": 0.8668216466903687
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8654289245605469,
        "score": 0.8654289245605469
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 653,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
      "originHit": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156"
    },
    {
      "chunkId": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d",
      "originHit": "knowledge-2-ed88478c0bcbcb415a81a9d2de2eee3151d83a77b0946a852c839467e7f7952d"
    },
    {
      "chunkId": "knowledge-3-f2288760b2100b5c59709aca8ba036fd87bf4d5aaddf8a644c04b56a5d8f7b60",
      "originHit": "knowledge-3-f2288760b2100b5c59709aca8ba036fd87bf4d5aaddf8a644c04b56a5d8f7b60"
    },
    {
      "chunkId": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c",
      "originHit": "knowledge-2-b1aa5f16d15b6265791515840c5fdd1c403d90f87cbf18bec2dbe226ee53aa2c"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    }
  ]
}
```

## Q278

제 계정의 현재 구독 상태를 확인해 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "CURRENT_STATE",
  "rationale": "개인 구독 상태 조회 필요",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q278",
  "group": "G139",
  "question": "제 계정의 현재 구독 상태를 확인해 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.120999999548076,
  "retrievalMs": 2.725599999394035,
  "hits": [
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8913457989692688,
      "score": 0.8913457989692688
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "denseScore": 0.8864481449127197,
      "score": 0.8864481449127197
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8789775371551514,
      "score": 0.8789775371551514
    },
    {
      "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
      "denseScore": 0.8770343065261841,
      "score": 0.8770343065261841
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8763524293899536,
      "score": 0.8763524293899536
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8913457989692688,
      "score": 0.8913457989692688
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "denseScore": 0.8864481449127197,
      "score": 0.8864481449127197
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "denseScore": 0.8789775371551514,
      "score": 0.8789775371551514
    },
    {
      "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
      "denseScore": 0.8770343065261841,
      "score": 0.8770343065261841
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "denseScore": 0.8763524293899536,
      "score": 0.8763524293899536
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8913457989692688,
        "score": 0.8913457989692688
      },
      {
        "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
        "denseScore": 0.8864481449127197,
        "score": 0.8864481449127197
      },
      {
        "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
        "denseScore": 0.8789775371551514,
        "score": 0.8789775371551514
      },
      {
        "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
        "denseScore": 0.8770343065261841,
        "score": 0.8770343065261841
      },
      {
        "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
        "denseScore": 0.8763524293899536,
        "score": 0.8763524293899536
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1461,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "originHit": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5"
    },
    {
      "chunkId": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66",
      "originHit": "knowledge-4-cd6fd3d1b1a04fb7a918cdb8eacd64afceb4291dff15bcc9c9765a1abb0a6b66"
    },
    {
      "chunkId": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156",
      "originHit": "knowledge-3-4ec0a9593703090227e2e72bb41d8f2aa398a5435e5e5d36f5296180beb16156"
    },
    {
      "chunkId": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590",
      "originHit": "knowledge-2-93504127a735dbfd05bf72c39a1af9fce360b3c32e709fd03e4afb2dc3aa7590"
    }
  ]
}
```

## Q281

제 상담을 담당하는 관리자 이름을 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "CURRENT_STATE",
  "rationale": "개인 상담 이력 조회 필요",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q281",
  "group": "G141",
  "question": "제 상담을 담당하는 관리자 이름을 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.841100000106962,
  "retrievalMs": 2.0666999989771284,
  "hits": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8489096164703369,
      "score": 0.8489096164703369
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8417007923126221,
      "score": 0.8417007923126221
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.840255081653595,
      "score": 0.840255081653595
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8397148251533508,
      "score": 0.8397148251533508
    },
    {
      "chunkId": "knowledge-6-e9f7fce1f09cfc09a971afdc8961f2cd8e62ba9e6762edeeba973d5eb8b40b4a",
      "denseScore": 0.8381351232528687,
      "score": 0.8381351232528687
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "denseScore": 0.8489096164703369,
      "score": 0.8489096164703369
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8417007923126221,
      "score": 0.8417007923126221
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.840255081653595,
      "score": 0.840255081653595
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8397148251533508,
      "score": 0.8397148251533508
    },
    {
      "chunkId": "knowledge-6-e9f7fce1f09cfc09a971afdc8961f2cd8e62ba9e6762edeeba973d5eb8b40b4a",
      "denseScore": 0.8381351232528687,
      "score": 0.8381351232528687
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
        "denseScore": 0.8489096164703369,
        "score": 0.8489096164703369
      },
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8417007923126221,
        "score": 0.8417007923126221
      },
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.840255081653595,
        "score": 0.840255081653595
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8397148251533508,
        "score": 0.8397148251533508
      },
      {
        "chunkId": "knowledge-6-e9f7fce1f09cfc09a971afdc8961f2cd8e62ba9e6762edeeba973d5eb8b40b4a",
        "denseScore": 0.8381351232528687,
        "score": 0.8381351232528687
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 719,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc",
      "originHit": "knowledge-6-aec93baf625be9cef096ea233350d9037ab6400319a11333efc68a1c7e8175dc"
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    },
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    },
    {
      "chunkId": "knowledge-6-e9f7fce1f09cfc09a971afdc8961f2cd8e62ba9e6762edeeba973d5eb8b40b4a",
      "originHit": "knowledge-6-e9f7fce1f09cfc09a971afdc8961f2cd8e62ba9e6762edeeba973d5eb8b40b4a"
    }
  ]
}
```

## Q282

지금 제 상담 담당자가 누구인지 조회해 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "CURRENT_STATE",
  "rationale": "개인 상담 이력 조회 필요",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q282",
  "group": "G141",
  "question": "지금 제 상담 담당자가 누구인지 조회해 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.641400000167778,
  "retrievalMs": 2.2541999987879535,
  "hits": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8513175249099731,
      "score": 0.8513175249099731
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8499998450279236,
      "score": 0.8499998450279236
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8458181023597717,
      "score": 0.8458181023597717
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8452182412147522,
      "score": 0.8452182412147522
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8444276452064514,
      "score": 0.8444276452064514
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "denseScore": 0.8513175249099731,
      "score": 0.8513175249099731
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "denseScore": 0.8499998450279236,
      "score": 0.8499998450279236
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8458181023597717,
      "score": 0.8458181023597717
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8452182412147522,
      "score": 0.8452182412147522
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "denseScore": 0.8444276452064514,
      "score": 0.8444276452064514
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
        "denseScore": 0.8513175249099731,
        "score": 0.8513175249099731
      },
      {
        "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
        "denseScore": 0.8499998450279236,
        "score": 0.8499998450279236
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8458181023597717,
        "score": 0.8458181023597717
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8452182412147522,
        "score": 0.8452182412147522
      },
      {
        "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
        "denseScore": 0.8444276452064514,
        "score": 0.8444276452064514
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1181,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661",
      "originHit": "knowledge-5-7ea4c0381106462c28d6ab1863b44e9de2cc4b13a5ca83dccfa462f766256661"
    },
    {
      "chunkId": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3",
      "originHit": "knowledge-6-0c8a410699d18162bb95df856e79b96c985b13e3474fdbbaed2ecf9222c96aa3"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f",
      "originHit": "knowledge-6-f1db1667958aa5c31e13b0b5ff73c3af83d130530260284021763d26edae0f1f"
    }
  ]
}
```

## Q287

파이썬 리스트 정렬 코드를 작성해 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "OUT_OF_SCOPE",
  "rationale": "서비스 범위 밖 프로그래밍",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q287",
  "group": "G144",
  "question": "파이썬 리스트 정렬 코드를 작성해 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.057499999878928,
  "retrievalMs": 2.7473999998619547,
  "hits": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8331417441368103,
      "score": 0.8331417441368103
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8327775001525879,
      "score": 0.8327775001525879
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8277283310890198,
      "score": 0.8277283310890198
    },
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8220879435539246,
      "score": 0.8220879435539246
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "denseScore": 0.8219185471534729,
      "score": 0.8219185471534729
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8331417441368103,
      "score": 0.8331417441368103
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8327775001525879,
      "score": 0.8327775001525879
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8277283310890198,
      "score": 0.8277283310890198
    },
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "denseScore": 0.8220879435539246,
      "score": 0.8220879435539246
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "denseScore": 0.8219185471534729,
      "score": 0.8219185471534729
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8331417441368103,
        "score": 0.8331417441368103
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8327775001525879,
        "score": 0.8327775001525879
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8277283310890198,
        "score": 0.8277283310890198
      },
      {
        "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
        "denseScore": 0.8220879435539246,
        "score": 0.8220879435539246
      },
      {
        "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
        "denseScore": 0.8219185471534729,
        "score": 0.8219185471534729
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1465,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5",
      "originHit": "knowledge-1-47c58fd360227c6ef7c4468bee885a4f0b0b5ef4e68e6b01e08716890275c5b5"
    },
    {
      "chunkId": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5",
      "originHit": "knowledge-6-e0bbb114ad15ee30a4da0e4f1661a94df91deef5c4b7876f69ffefe62139ffb5"
    }
  ]
}
```

## Q288

파이썬 배열을 오름차순으로 정렬하는 코드를 알려주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "OUT_OF_SCOPE",
  "rationale": "서비스 범위 밖 프로그래밍",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q288",
  "group": "G144",
  "question": "파이썬 배열을 오름차순으로 정렬하는 코드를 알려주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 12.012400000458001,
  "retrievalMs": 2.505800001017633,
  "hits": [
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8461310863494873,
      "score": 0.8461310863494873
    },
    {
      "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
      "denseScore": 0.8423265814781189,
      "score": 0.8423265814781189
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8395000696182251,
      "score": 0.8395000696182251
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8332087397575378,
      "score": 0.8332087397575378
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.832446813583374,
      "score": 0.832446813583374
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8461310863494873,
      "score": 0.8461310863494873
    },
    {
      "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
      "denseScore": 0.8423265814781189,
      "score": 0.8423265814781189
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8395000696182251,
      "score": 0.8395000696182251
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "denseScore": 0.8332087397575378,
      "score": 0.8332087397575378
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.832446813583374,
      "score": 0.832446813583374
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8461310863494873,
        "score": 0.8461310863494873
      },
      {
        "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
        "denseScore": 0.8423265814781189,
        "score": 0.8423265814781189
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8395000696182251,
        "score": 0.8395000696182251
      },
      {
        "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
        "denseScore": 0.8332087397575378,
        "score": 0.8332087397575378
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.832446813583374,
        "score": 0.832446813583374
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1487,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830",
      "originHit": "knowledge-1-bf55c858fe5a421e1181ff8ec31b9c00cd0e846a43c568d8f29f0f94999e1830"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38",
      "originHit": "knowledge-5-d2ce31ec3a27afeca3d5ad1dc52ac14ea5cd2ca86e3653f67bf7618e8c481c38"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    }
  ]
}
```

## Q289

내일 어떤 주식을 사면 수익이 날까요?

### 기대 근거·처리

```json
{
  "expectedRoute": "OUT_OF_SCOPE",
  "rationale": "서비스 범위 밖 금융",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q289",
  "group": "G145",
  "question": "내일 어떤 주식을 사면 수익이 날까요?",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 9.826800000155345,
  "retrievalMs": 2.4597999999969034,
  "hits": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8247774243354797,
      "score": 0.8247774243354797
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8236005902290344,
      "score": 0.8236005902290344
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8231567740440369,
      "score": 0.8231567740440369
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8194597959518433,
      "score": 0.8194597959518433
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8192315101623535,
      "score": 0.8192315101623535
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8247774243354797,
      "score": 0.8247774243354797
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "denseScore": 0.8236005902290344,
      "score": 0.8236005902290344
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "denseScore": 0.8231567740440369,
      "score": 0.8231567740440369
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "denseScore": 0.8194597959518433,
      "score": 0.8194597959518433
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "denseScore": 0.8192315101623535,
      "score": 0.8192315101623535
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8247774243354797,
        "score": 0.8247774243354797
      },
      {
        "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
        "denseScore": 0.8236005902290344,
        "score": 0.8236005902290344
      },
      {
        "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
        "denseScore": 0.8231567740440369,
        "score": 0.8231567740440369
      },
      {
        "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
        "denseScore": 0.8194597959518433,
        "score": 0.8194597959518433
      },
      {
        "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
        "denseScore": 0.8192315101623535,
        "score": 0.8192315101623535
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1408,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1",
      "originHit": "knowledge-4-70412fbde93487dbdf980f7ffa2683de57352b3a7ecda76636e9ceef0f941cb1"
    },
    {
      "chunkId": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56",
      "originHit": "knowledge-1-79720b6fb54419be7efe4a19d9e05ff1b0ce90a03d633286cd3efdfca33ccb56"
    },
    {
      "chunkId": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313",
      "originHit": "knowledge-3-f4c461585b2f1b50a91cbfbb4c751fcb9e8409bcfb27309e3619a3a9785dc313"
    },
    {
      "chunkId": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034",
      "originHit": "knowledge-1-24720e832e930d594bf680c22cd76a789386a01cd8516595a98cbdc460688034"
    }
  ]
}
```

## Q290

다음 주 급등할 종목을 추천해 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "OUT_OF_SCOPE",
  "rationale": "서비스 범위 밖 금융",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q290",
  "group": "G145",
  "question": "다음 주 급등할 종목을 추천해 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.410599999886472,
  "retrievalMs": 2.021199999944656,
  "hits": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8408306837081909,
      "score": 0.8408306837081909
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8377755880355835,
      "score": 0.8377755880355835
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.8339540958404541,
      "score": 0.8339540958404541
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8325191736221313,
      "score": 0.8325191736221313
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8321229219436646,
      "score": 0.8321229219436646
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8408306837081909,
      "score": 0.8408306837081909
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8377755880355835,
      "score": 0.8377755880355835
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.8339540958404541,
      "score": 0.8339540958404541
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8325191736221313,
      "score": 0.8325191736221313
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8321229219436646,
      "score": 0.8321229219436646
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8408306837081909,
        "score": 0.8408306837081909
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8377755880355835,
        "score": 0.8377755880355835
      },
      {
        "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
        "denseScore": 0.8339540958404541,
        "score": 0.8339540958404541
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8325191736221313,
        "score": 0.8325191736221313
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8321229219436646,
        "score": 0.8321229219436646
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 858,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "originHit": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    }
  ]
}
```

## Q295

봄을 주제로 시를 써주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "OUT_OF_SCOPE",
  "rationale": "서비스 범위 밖 창작",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q295",
  "group": "G148",
  "question": "봄을 주제로 시를 써주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 10.198700001637917,
  "retrievalMs": 2.48239999928046,
  "hits": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8126852512359619,
      "score": 0.8126852512359619
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.812106192111969,
      "score": 0.812106192111969
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8047442436218262,
      "score": 0.8047442436218262
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.8028772473335266,
      "score": 0.8028772473335266
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.8019213080406189,
      "score": 0.8019213080406189
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8126852512359619,
      "score": 0.8126852512359619
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.812106192111969,
      "score": 0.812106192111969
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8047442436218262,
      "score": 0.8047442436218262
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "denseScore": 0.8028772473335266,
      "score": 0.8028772473335266
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "denseScore": 0.8019213080406189,
      "score": 0.8019213080406189
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8126852512359619,
        "score": 0.8126852512359619
      },
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.812106192111969,
        "score": 0.812106192111969
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8047442436218262,
        "score": 0.8047442436218262
      },
      {
        "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
        "denseScore": 0.8028772473335266,
        "score": 0.8028772473335266
      },
      {
        "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
        "denseScore": 0.8019213080406189,
        "score": 0.8019213080406189
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1159,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12",
      "originHit": "knowledge-1-1d0103ecf36fd805f4fbd8c91570deb671816e82cce13cc8fc14c638e8680e12"
    },
    {
      "chunkId": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380",
      "originHit": "knowledge-1-3d483831028b7d26d4c6d31af1983b43ef100106aecc27fc3042ffce23215380"
    }
  ]
}
```

## Q296

봄 풍경을 묘사한 짧은 시를 만들어 주세요.

### 기대 근거·처리

```json
{
  "expectedRoute": "OUT_OF_SCOPE",
  "rationale": "서비스 범위 밖 창작",
  "gold": []
}
```

### 실제 검색 결과 전체

```json
{
  "id": "Q296",
  "group": "G148",
  "question": "봄 풍경을 묘사한 짧은 시를 만들어 주세요.",
  "method": "R1",
  "split": "final",
  "queryEmbeddingMs": 11.044699998819851,
  "retrievalMs": 2.237199998489814,
  "hits": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8164880871772766,
      "score": 0.8164880871772766
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8153923749923706,
      "score": 0.8153923749923706
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8061397075653076,
      "score": 0.8061397075653076
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8055516481399536,
      "score": 0.8055516481399536
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8032557964324951,
      "score": 0.8032557964324951
    }
  ],
  "candidates": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "denseScore": 0.8164880871772766,
      "score": 0.8164880871772766
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "denseScore": 0.8153923749923706,
      "score": 0.8153923749923706
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "denseScore": 0.8061397075653076,
      "score": 0.8061397075653076
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "denseScore": 0.8055516481399536,
      "score": 0.8055516481399536
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "denseScore": 0.8032557964324951,
      "score": 0.8032557964324951
    }
  ],
  "components": {
    "dense": [
      {
        "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
        "denseScore": 0.8164880871772766,
        "score": 0.8164880871772766
      },
      {
        "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
        "denseScore": 0.8153923749923706,
        "score": 0.8153923749923706
      },
      {
        "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
        "denseScore": 0.8061397075653076,
        "score": 0.8061397075653076
      },
      {
        "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
        "denseScore": 0.8055516481399536,
        "score": 0.8055516481399536
      },
      {
        "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
        "denseScore": 0.8032557964324951,
        "score": 0.8032557964324951
      }
    ]
  },
  "omittedChunkIds": [],
  "contextTokens": 1042,
  "decision": "CANDIDATES_ONLY",
  "evaluation": {
    "answerable": false,
    "checks": [],
    "allPolicies": null,
    "allAnchors": null,
    "allSourceClauses": null,
    "nonGoldContextChunks": null,
    "nonPolicyQuestionReturnedCandidates": true,
    "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
    "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR"
  },
  "contextReferences": [
    {
      "chunkId": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230",
      "originHit": "knowledge-7-5ecea2af307332bcda55770aa0012ab9479b16dc92429aab1275b618dae34230"
    },
    {
      "chunkId": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032",
      "originHit": "knowledge-1-19b7b5cf7a51dacbb292e4c6509af2a7f097d77471ec08746bbc087ab9cf5032"
    },
    {
      "chunkId": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938",
      "originHit": "knowledge-6-879d21a68a0d59271db706330c6dd3eeae6e46174f2b5184400e1b968b76f938"
    },
    {
      "chunkId": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a",
      "originHit": "knowledge-1-c9ff20281e0a4c58faadb97dae96f9951bba5110d20de9f8d78ac13dd92fa02a"
    },
    {
      "chunkId": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9",
      "originHit": "knowledge-5-efaa8afb43b631cd9131f7d4ba3a380cd442970c5be9b1231879606ce221a9b9"
    }
  ]
}
```

