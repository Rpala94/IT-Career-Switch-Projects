const getSleepHours = day  => {

    // ELse Statement and Else IF statement
      /*  if (day === 'monday'){
            return 8;
        } else if (day === 'tuesday'){
            return 7;
        } else if (day === 'wednesday'){
            return 6;
        }else if (day === 'thursday'){
            return 5;
        }else if (day === 'friday'){
            return 4;
        }else if (day === 'saturday'){
            return 3;
        }else if (day === 'sunday'){
            return 2;
        } else {
    
        }*/
    
    // Switch Statement
    
        switch(day){
            case 'monday':
                return 8;
                break;
                case 'tuesday':
                    return 7;
                    break;
                    case 'wednesday':
                        return 8;
                        break;
                        case 'thursday':
                            return 8;
                            break;
                            case 'friday':
                                return 5;
                                break;
                                case 'saturday':
                                    return 8;
                                    break;
                                    case 'sunday':
                                        return 12;
                                        break;
    
                                        default: 
                                        return "Error!";
        }
    };
    
    
    
    const getActualSleepHours = () =>  getSleepHours('monday') + 
        getSleepHours('tuesday')+
        getSleepHours('wednesday')+
        getSleepHours('thursday')+
        getSleepHours('friday')+
        getSleepHours('saturday')+
        getSleepHours('sunday');
    
    
        console.log(getSleepHours('monday'));
        console.log(getActualSleepHours());
    
    
        const getIdealSleepHours = () => {
          let idealHours = 8;
          return idealHours * 7;
        };
    
    
        const calculateSleepDebt = () => {
            const actualSleepHours = getActualSleepHours();
            const IdealSleepHours = getIdealSleepHours();
        
            if(actualSleepHours === getIdealSleepHours) {
                console.log("You've got the perfect amount of sleep this week!");
            } else if(actualSleepHours > IdealSleepHours) {
                console.log("You've got " + (actualSleepHours-IdealSleepHours) + 
                " more hours of sleep this week.");
            } else if(actualSleepHours < IdealSleepHours) {
                console.log("You should get some rest because you've slept " + (IdealSleepHours-actualSleepHours) + " hours less than you should have this week.");
            } else {
                console.log("Error! Something went wrong, check your code.");}
        };
    
        calculateSleepDebt();