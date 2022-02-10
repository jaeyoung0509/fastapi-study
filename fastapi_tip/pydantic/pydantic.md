## What is orm_mode ?

> pydantic description
 * ORM Mode (aka Arbitrary Class Instances)
Pydantic models can be created from arbitrary class instances to support models that map to ORM objects.
 * 1. The Config property orm_mode must be set to True.
* 2. The special constructor from_orm must be used to create the model instance.
* 3. from_orm()모드를 통해 손쉽게 모델 변환도 가능 
> 뇌피셜

* orm_mode를 통해 sqlalchemy orm객체를 -> pydantic으로 변환 해
 response_model = pydantic_model로 정의 가능

## relationship
> * pydantic BaseModel을 상속받은 클래스를 재 상속 가능
* 주의: 스크립트 언어이기 떄문에 부모 클래스를 위에 기술 해야 됨
