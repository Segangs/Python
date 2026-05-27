#로깅
# 다 보고 싶으면 레벨을 디버그 수준으로 하면 된다. (디버그 인포 워닝 에러 크리티컬 순)

import logging

def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S", filename="logger.log", encoding="utf-8")
    logging.debug("디버그 메세지 입니다.")
    logging.info("프로그램 시작")
    logging.warning("프로그램 종료 직전입니다.")
    

        
    
if __name__ == "__main__":
    main()