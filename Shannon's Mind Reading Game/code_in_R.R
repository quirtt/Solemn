#Cards is the permutation _Sigma_.

Dataset = c(26,26,24,26,26,25,26,26,25,23,25,26,24,26,24,26,26,23,20,26,23,22,25,23,26,26,23,25,23,25,25,25,25,26,25,23,25,24,26,25,26,23,26,23,26,24,26,24,25,24,25,23,24,25,22,21,25,25,25,21,23,24,23,21,26,25,25,24,24,25,24,25,24,24,23,25,21,25,26,26,23,25,25,23,21,24,21,25,25,22,24,25,26,23,24,25,19,25,23,25)


RiffleShuffle <- function(Cards){
  ### Riffle shuffles the vector of Cards using
  ### L/(L+R), R/(L+R) probabilities to each hand. 
  NewDeck = vector()
  split = floor(rnorm(1, mean=25.78, sd = 2.3046))

  LeftHand = Cards[1:split]
  RightHand = Cards[(split+1):52]
  for(x in 1:52){
    L <- length(LeftHand)
    R <- length(RightHand)
    hand = sample(c("L", "R"), 1, prob=c(L,R))
    
    if(hand == "L"){
      card = LeftHand[1]
      LeftHand <- if (L != 1) LeftHand[2:L] else vector()
      NewDeck = append(NewDeck, card)
    }
    else{
      card = RightHand[1]
      RightHand <- if (R != 1) RightHand[2:R] else vector()
      NewDeck = append(NewDeck, card)
    }
  }
  
  return(NewDeck)
}

Switch <- function(Cards, vals) {
  # 1 <= y <= 52
  # 1 <= x <= 52
  # Logic: xth index card is moved at yth index
  x = vals[1]
  y = vals[2]
  NewCards = vector()
  for (i in 1:length(Cards)) {
    if (i != x) {
      NewCards = append(NewCards, Cards[i])
    }
  }
  if (y != 1) {
    if (y != 52) {
      NewCards = append(NewCards, Cards[x], after = y - 1)
    } else {
      NewCards = append(NewCards, Cards[x])
    }
  } else {
    NewCards = append(Cards[x], NewCards)
  }
  return(NewCards)
}

RisingSingleton <- function(array){
  ### Checks if there is a unique Rising Singleton and returns the singleton.
  index = numeric(0)
  for (i in 1:52){
    index[array[i]] = i
  }
  Sum = 0
  SingletonCard = 0
  for (i in 1:52){
    if((index[i] >= index[min((i+1), 52)]) & (index[i] <= index[max((i-1), 1)])){
      Sum = Sum + 1
      SingletonCard = i
    }
  }
  return(c((Sum == 1), SingletonCard))
}

Process <- function(Cards){
  ### Performs the whole process and outputs whether there
  ### is a unique Rising Singleton
  Cards = RiffleShuffle(Cards)
  Cards = RiffleShuffle(Cards)
  Cards = RiffleShuffle(Cards)
  
  vals = c(1, rbinom(1, 52, 0.5))
  PickedCard = Cards[1]
  Cards = Switch(Cards, vals)

  RSCheck = RisingSingleton(Cards)
  return((RSCheck[1])&(RSCheck[2] == PickedCard))
}

SumCalculator <- function(Cards){
  ### Simulates Process 10000 and counts how many times  
  ### there is a unique Rising Singleton which is also indeed
  ### the picked card.
  Sum = 0
  for(i in 1:10000){
    Sum = Sum + Process(Cards)
  }
  return(Sum)
}

Cards = 1:52
SumCalculator(Cards)/10000 * 100