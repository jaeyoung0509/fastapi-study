from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DBURL = ''
engine = create_engine(DBURL , pool_pre_ping= True)

'''
"pre ping" 기능은 일반적으로 풀에서 연결이 체크아웃될 때마다 "SELECT 1"에 해당하는 SQL을 내보냅니다. "연결 끊김" 상황으로 감지된 오류가 발생하면 연결이 즉시 재활용되고 현재 시간보다 오래된 다른 모든 풀링된 연결이 무효화되어 다음에 체크아웃할 때도 재활용됩니다
'''
SessionLocal = sessionmaker(autocommit= False , autoflush= False , bind=engine)