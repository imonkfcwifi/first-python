from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_Url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_Url}{keyword}")
    if response.status_code != 200:
        print("cant request")
    else:
        results =[]
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_='jobs')
        # class가 jobs인 section들을 찾기
        # class라는 keyword는 이미 python에서 사용하고있기때문에 class_
        # if나 else를 변수명으로 설정할수없는것과 같다
        for job in jobs:
            job_post = job.find_all('li')
            # find _all은 list를 가져오고 find는 결과를 가져옴
            job_post.pop(-1)
            for post in job_post:
                anchors = post.find_all('a') 
                anchor = anchors[1]
                link = anchor['href']
                company , kind, region = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_='title')
                job_data_dict = {
                    'company' : company.string,
                    'kind' : kind.string,
                    'region' : region.string,
                    'title' : title.string
                }
                results.append(job_data_dict)
                # 이렇게 외부 저장소에 저장해주면 작업이 끝난 이후에도 사라지지 않음
        return results

