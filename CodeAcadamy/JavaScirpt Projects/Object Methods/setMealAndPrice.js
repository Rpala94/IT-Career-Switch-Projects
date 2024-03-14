const menu = {
    _menu: '',
    _price: 0,
  
    set meal(mealToCheck){ //Setting the input to be recognized as a string
      if (typeof mealToCheck === 'string'){
        return this._meal = mealToCheck;
      }
  
    },
    set price(priceToCheck){ //Setting the input to be recognized as a number
      if (typeof priceToCheck === 'number') {
        return this._price = priceToCheck;
      }
    },
  
    get todaySpecial() { //If statement for today's special and return error message for input
      if (this._meal && this._price) {
        return `Today's Meal is ${this._meal} for £${this._price}!`
      } else {
        return 'Meal or Price not set correctly!'
      }
    }
    
  };
  
  menu._meal = 'Pizza';
  menu._price = 8;
  console.log(menu.todaySpecial);
  
  