const toEmoticon = (meaning) => {
    switch (meaning) {
      case 'shrug':
      return '|_{"}_|';
      case 'smiley face':
      return ':)';
      case 'frowny face':
      return ':(';
      case 'winky face':
      return ';)';
      case 'heart':
      return '<3';
      default:
      return '|_(* ~ *)_|';
    }
  }
  
  
  
   console.log(toEmoticon("whatever")) // Should print  '|_(* ~ *)_|'
   console.log(toEmoticon('smiley face'))
   console.log(toEmoticon('heart'))
  
  