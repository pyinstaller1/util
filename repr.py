import re
import json

def get_json_week(data_list):
    stats = {}

    for entry in data_list:

        # 1. 메인 카테고리명 추출 (○ 뒤의 텍스트)
        # 예: "AAA 건강자격조회"
        title = re.search(r"○\s*([A-Z]+ [가-힣]+)", entry)

        if not title: continue
        category = title.group(1)


        

        # 2. 하위 서버별 건수 추출 (- 뒤의 텍스트)
        # 예: [('자격1서버', '30'), ('자격2서버', '30')]
        server_matches = re.findall(r"-\s*([가-힣0-9]+)\s*(\d+)건", entry)

        # 3. 데이터 구조 초기화 (중복 합치기용)
        if category not in stats:
            stats[category] = {
                "total_sum": 0,      # 해당 업무 전체 건수 합계
                "total_freq": 0,     # 해당 업무 보고 횟수(빈도)
                "server_details": {} # 하위 서버별 상세 통계
            }

        
        # 메인 카테고리 빈도 누적
        stats[category]["total_freq"] += 1

        for s_name, s_count in server_matches:
            count = int(s_count)
            
            # 서버 데이터 구조 초기화
            if s_name not in stats[category]["server_details"]:
                stats[category]["server_details"][s_name] = {
                    "sum": 0,        # 서버별 건수 합계
                    "freq": 0        # 서버별 노출 빈도
                }
            
            # 하위 서버별 합계 및 빈도 누적
            stats[category]["server_details"][s_name]["sum"] += count
            stats[category]["server_details"][s_name]["freq"] += 1
            
            # 메인 카테고리 전체 합계 누적
            stats[category]["total_sum"] += count

    return stats




def report_week(stats_dict):
    """
    메신저 폭에 최적화된 슬림 리포트 (에러 수정 완료)
    """

    # 1. 정렬 (빈도 높은 순 -> 건수 많은 순)
    sorted_items = sorted(
        stats_dict.items(), 
        key=lambda x: (x[1]['total_freq'], x[1]['total_sum']), 
        reverse=True
    )
    
    # 2. 메신저용 출력 시작
    print("▣" * 15)
    print(" [서버 점검 순위 보고]")
    print("▣" * 15)
    print(f"{'순위'} {'대상업무':<12} {'빈도/합계'}")
    print("-" * 28)

    for i, (category, data) in enumerate(sorted_items, 1):
        # 업무명 가독성 정리
        name = category.replace("_", " ")[:12]
        
        # 메인 정보 (빈도와 전체 합계)


        if i<100:
            print(f"{i}위 {name}")
            print(f"    ▶ {data['total_freq']}회 | {data['total_sum']:,}건")

            # 서버 상세 (키 이름을 'freq', 'sum'으로 정확히 매칭)
            for s_name, s_info in data['server_details'].items():
                # s_info['freq']와 s_info['sum']을 사용하여 KeyError 방지
                print(f"     └ {s_name}: {s_info['freq']}회({s_info['sum']:,}건)")
        
        print("-" * 28)

    print("※ 빈도: 7일간 보고 횟수")
    print("※ 합계: 누적 건수 총합")
    print("▣" * 15)


















list_repr = [
    ' ○ AAA 건강자격조회 외 100건\n   - 자격1서버 30건\n   - 자격2서버 30건',
    ' ○ BBB 급여제공 외 100건\n   - 급여1서버 30건\n   - 급여2서버 130건',
    ' ○ AAA 건강자격조회 외 90건\n   - 자격1서버 45건\n   - 자격2서버 45건',
    ' ○ CCC 장기요양 외 80건\n   - 장기1서버 40건\n   - 장기2서버 40건',
    ' ○ CCC 장기요양 외 80건\n   - 장기1서버 40건\n   - 장기2서버 40건',
    ' ○ BBB 급여제공 외 85건\n   - 급여1서버 40건\n   - 급여2서버 45건',
    ' ○ BBB 급여제공 외 85건\n   - 급여1서버 40건\n   - 급여2서버 45건',
    ' ○ AAA 건강자격조회 외 120건\n   - 자격1서버 60건\n   - 자격2서버 60건',
    ' ○ BBB 급여제공 외 150건\n   - 급여1서버 50건\n   - 급여2서버 100건',
    ' ○ CCC 장기요양 외 110건\n   - 장기1서버 55건\n   - 장기2서버 55건',
    ' ○ BBB 급여제공 외 100건\n   - 급여1서버 30건\n   - 급여2서버 130건',
    ' ○ AAA 건강자격조회 외 95건\n   - 자격1서버 45건\n   - 자격2서버 50건',
    ' ○ BBB 급여제공 외 110건\n   - 급여1서버 50건\n   - 급여2서버 60건',
    ' ○ AAA 건강자격조회 외 110건\n   - 자격1서버 55건\n   - 자격2서버 55건',
    ' ○ CCC 장기요양 외 90건\n   - 장기1서버 45건\n   - 장기2서버 45건',
    ' ○ AAA 건강자격조회 외 100건\n   - 자격1서버 30건\n   - 자격2서버 30건',
    ' ○ BBB 급여제공 외 100건\n   - 급여1서버 30건\n   - 급여2서버 130건',
    ' ○ CCC 장기요양 외 80건\n   - 장기1서버 40건\n   - 장기2서버 40건',
    ' ○ AAA 건강자격조회 외 100건\n   - 자격1서버 30건\n   - 자격2서버 30건',
    ' ○ BBB 급여제공 외 100건\n   - 급여1서버 30건\n   - 급여2서버 130건'
]


result = get_json_week(list_repr)
report_week(result)














