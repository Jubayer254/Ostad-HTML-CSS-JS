// dom element select
const spinner = document.getElementById("spinner");
const food_list = document.getElementById("food-list");
const searchBtn = document.getElementById("searchBtn");
const searchField = document.getElementById("searchField");
const modal_content = document.getElementById("modal-content");
const scrollToTop = document.getElementById("scrollToTop");

//event listener
window.addEventListener('load', initial_load);
window.addEventListener('scroll', scrolling);
searchBtn.addEventListener('click', searchFood);
scrollToTop.addEventListener('click', scrollingToTop);

// functionality

async function initial_load(){
    const api_url = `https://www.themealdb.com/api/json/v1/1/search.php?s`;
    const foods = await get_data(api_url);
    showFood(foods.meals);
}

async function get_data(api_url){
    try{
    
        const res = await fetch(api_url);
        const data = await res.json();
        spinner.classList.add('hidden');
        
        return data;
    }catch(error){
        console.log(error);
    }
}

function showFood(foods){
    let foodItem = ''
    foods.forEach(food => {
        foodHTML = `
        <div class="food-item">
            <div class="card card-compact bg-base-100 shadow-xl">
                <figure>
                    <img
                    class="w-full h-60 object-cover"
                    src="${food.strMealThumb}"
                    alt="images"
                    />
                </figure>
                <div class="card-body">
                    <h2 class="card-title">${food.strMeal}</h2>
                    <p>
                    ${food.strInstructions.slice(0, 120)}
                    </p>
                    <div class="card-actions justify-end">
                    <label
                        onClick="modal(${food.idMeal})"
                        for="my-modal-6"
                        class="btn btn-warning text-white"
                        >View Details</label
                    >
                    </div>
                </div>
            </div>
        </div>
        `
        foodItem = foodItem + foodHTML;
        
    });
    food_list.innerHTML = foodItem;
}

async function searchFood(){
    let searchFieldText  = searchField.value;
    const api_url = `https://www.themealdb.com/api/json/v1/1/search.php?s=${searchFieldText}`;
    spinner.classList.remove('hidden');
    food_list.innerHTML = ""
    const foods = await get_data(api_url);
    if (foods.meals == null){
        food_list.innerHTML = "<h2>No food found</h2>"
        return;
    }
    else{
        showFood(foods.meals);
    }    
}

async function modal(id){
    modal_content.innerHTML = ""

    const api_url = `https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`;
    const food = await get_data(api_url);
    
    let ModalHtml = `
        <div class="card card-compact bg-base-100 shadow-xl">
            <figure>
              <img
                class="w-full h-96 object-cover"
                src="${food.meals[0].strMealThumb}"
                alt="images"
              />
            </figure>
            <div class="card-body">
              <h2 class="card-title">${food.meals[0].strMeal}</h2>
              <p>
                ${food.meals[0].strInstructions}
              </p>
            </div>
        </div>
    `
    modal_content.innerHTML = ModalHtml
}

function scrollingToTop(){
    window.scrollTo({top: 0, behavior:"smooth"})
}

function scrolling(){
    const px = window.scrollY;

    if (px > 200){
        scrollToTop.style.opacity = 1;
        scrollToTop.style.visiblity = 'visible';
    }
    else{
        scrollToTop.style.opacity = 0;
        scrollToTop.style.visiblity = 'hidden';
    }

}