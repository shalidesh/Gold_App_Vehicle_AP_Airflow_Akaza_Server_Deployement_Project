import { useContext, useRef,useEffect,useState } from "react";
import './news.css';
import axios from "axios";

function NewsTitles() {

    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/api/user/news');
                setData(response.data)          
                
            } catch (error) {
                console.log("Error2:", error);
            }
        }
        fetchData();
    }, []);


        return (

            <div>
                    <section class="light">
                        <div class="container py-2">
                            
                                <div class="h1 text-center text-dark" id="pageHeaderTitle">Latest Gold News</div>

                                {data.map((item, index) => (

                                    <article class="postcard light blue">
                                        <a class="postcard__img_link" href="#">
                                            <img class="postcard__img" src={item.post_img} alt="Image Title" />
                                        </a>
                                        <div class="postcard__text t-dark">
                                            <h1 class="postcard__title blue"><a href="#">{item.posted_title}</a></h1>
                                            <div class="postcard__subtitle small">
                                                <time datetime="2020-05-25 12:00:00">
                                                    <i class="fas fa-calendar-alt mr-2"></i>{item.posted_date}
                                                </time>
                                            </div>
                                            <div class="postcard__bar"></div>
                                            <div class="postcard__preview-txt">{item.sample_text}</div>
                                            <ul class="postcard__tagbox">
                                                <li class="tag__item">
                                                    <a href={item.post_link} target="_blank" ><i class="fas fa-tag mr-2"></i>READ MORE</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </article>
                                ))}
        
                        </div>
                    </section>
                    
            </div>
  )
}

export default NewsTitles