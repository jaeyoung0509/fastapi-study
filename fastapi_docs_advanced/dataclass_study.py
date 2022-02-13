from dataclasses import dataclass
from datetime import date
'''
기존 클래스 작성
단점:
*   bolier-plate : 반복적으로 비슷한 형태를 띄는 코드
*   두개 인스턴스의 동등성  
    user1 ,user2가 동등한 필드를 갖고 있음에도 다른 인스턴스로 취급 
'''
class User_plain:
    def __init__(self) -> None:
        id : int  
        name : str 
        birth_date : date  
        admin : bool = False


'''
data class 사용하기
데이터 클래스는 __init__(), __repr__(), __eq__()와 같은 메서드를 자동으로 생성
option 
*   불변데이터 만들기(immutability)
    frozen=True
*   데이터 대소비교 및 정렬하기
    option = True

*   set  , dict에서 사용하기
    기본적으로 데이터클래스의 인스턴스는 hashtable하지 않기 때문에 , set 이나 dict로 바꿀수 가 없음
    unsafe_hash = True

*   list 같은 가변 데이터 사용하기
    from dataclasses import dataclass, field
    friends: List[int] = field(default_factory=list)

'''



@dataclass
class User:
    id :int 
    name : str 
    birth_date : date
    admin : bool = False

