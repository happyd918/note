# Javascript

### let, const



### Arrow Function

```js
function myFnc() {
    ...
}
const myFnc = () => {
    ...
}
```

```js
// 변수가 하나일 경우 소괄호 생략 가능
const printMyName = (name) => {
    console.log(name)
}

const printMyName = name => {
    console.log(name)
}
```

```js
// return 만 있으면 제외 가능
const multiply = (number) => {
    return number * 2
}

const multiply = number => number * 2
```



### Exports & Imports (Modules)

```js
// person.js  // default export
const person = {
    name: 'Max'
}

export default person
```

```js
// utility.js  // named export
export const clean = () => {...}
export const baseData = 10
```

```js
// app.js
import person from './person.js'
import prs from './person.js'

import { clean } from './utility.js'
import { baseData } from './utility.js'
```

- `export default`는 `person.js` 파일을 `import`해올 때 `export default` 뒤에 있는 것을 불러온다. 따라서 `import`를 `person`으로하든 `prs`로 하든 불러오는 것은 `person.js`의 `person`이다.
- 그냥 `import` 같은 경우(`utility.js`) 정확한 것을 지정하기 위해 중괄호로 감싸서 지정해줘야 한다.

```js
import { clean as cln } from './utility'
import * as bundle from './utility'
```



### Class

```js
class Person {
    name = 'Taehak'			// property
    call = () => {...}		// method
}
```

- `extends`

```js
class Human {
    constructor() {
        this.gender = 'male'
    }
    
    printGender() {
        console.log(this.gender)
    }
}

class Person extends Human {
    constructor() {
        super()		// constructor 하려면 써야함
        this.name = 'Taehak'
        // this.gender = 'female'
    }
    
    printMyName() {
        console.log(this.name)
    }
}

const person = new Person()
person.printMyName() // Taehak
person.printGender() // male // female
```



# es7

- es6

```js
constructor() {
    this.myProperty = 'value'
}

myMethod() {...}
```

- es7

```js
myProperty = 'value'

myMethod = () => {...}
```

- 비교(위 `class`참고)

```js
class Human {
    gender = 'male'
    
    printGender = () => {
        console.log(this.gender)
    }
}

class Person extends Human {
    name = 'Taehak'
    // gender = 'female'
    
    printMyName = () => {
        console.log(this.name)
    }
}
```



### Spread, Rest, Operators

> `...`

- Spread

  ```js
  const newArray = [...oldArray, 1, 2]
  const newObject = {...oldObject, newProp:5}
  ```

  

- Rest

  ```js
  function sortArgs(...args){
      return args.sort()
  }
  // 결과는 배열 Array 
  ```



### Destructuring

- Array Desturcturing

  ```js
  [a, b] = ['Hello', 'Taehak']
  console.log(a)	// Hello
  console.log(b)	// Taehak
  ```

  

- Object Destructuring

  ```js
  {name} = {name:'taehak', age:28}
  console.log(name) 	// taehak
  console.log(age)	// undefined
  ```

  

### 참조 주의

```js
const person = {
    name: 'taehak'
}

const secondPerson = person

const thirdPerson = {
    ...person
}

person.name = 'kim'

console.log(secondPerson)	// {name: 'kim'}
console.log(thirdPerson)	// {name: 'taehak'}
```



### map

```js
const numbers = [1, 2, 3]

const doubleNumbers = numbers.map((num) => {
    return num * 2
})

console.log(doubleNumbers)	// [2, 4, 6]
```

- `num`에는 아무거나 써두 됨



### 기타 함수들

`map, find, findIndex, filter, concat, slice, splice`