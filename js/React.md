# React

> js 라이브러리



### Components of React

- 웹 프로그래밍의 함수 같은거
- 구성요소들



### 선언적 방식 Declarative Approach



### React Start

```
npx create-react-app my-app
```

- `create-react-app`



### 1. npm start

- `index.js`가 가장 먼저 실행됨

  ```js
  import ReactDOM from 'react-dom/client';
  
  import './index.css';		// css는 써야하고
  import App from './App';	// .js 확장자 빼야함
  
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(<App />);
  ```

  - `import './index.css';` 이런거 실행시켜줌
  - `<App />` 이런것도 실행시켜줌



### 2. JSX

```react
function App() {
  return (
    <div>
      <h2>Let's get started!</h2>
    </div>
  );
}

export default App;

```

- `return`안에는 한개의 객체가 있어야
- `class` 지정하고 싶으면 `className`으로 지정



### 3. Custom Components

- `ExpenseItem.js` 

```react
// src/components/ExpenseItem.js
function ExpenseItem() {
  return (
    <h2>Expense item!</h2>
  )
}

export default ExpenseItem
```

- `app.js`

```react
import ExpenseItem from "./components/ExpenseItem";

function App() {
  return (
    <div>
      <h2>Let's get started!</h2>
      <ExpenseItem></ExpenseItem>
    </div>
  );
}

export default App;

// import 해주고 JSX 안에서 custom 컴포넌트를 쓰려면 대문자로 시작하는 태그로 작성해야 인식가능
```



### 4. Props

```react
import './ExpenseItem.css'

function ExpenseItem(props) {
  return (
    <div className='expense-item'>
      <div>{props.date.toISOString()}</div>
      <div className='expense-item__description'>
        <h2>{props.title}</h2>
        <div className='expense-item__price'>{props.amount}</div>
      </div>
    </div>
  )
}

export default ExpenseItem
```

```react
import ExpenseItem from "./components/ExpenseItem";

function App() {
  const expenses = [
    {
      id: 'e1',
      title: 'Toilet Paper',
      amount: 94.12,
      date: new Date(2020, 7, 14),
    },
    { id: 'e2', title: 'New TV', amount: 799.49, date: new Date(2021, 2, 12) },
    {
      id: 'e3',
      title: 'Car Insurance',
      amount: 294.67,
      date: new Date(2021, 2, 28),
    },
    {
      id: 'e4',
      title: 'New Desk (Wooden)',
      amount: 450,
      date: new Date(2021, 5, 12),
    },
  ];

  return (
    <div>
      <h2>Let's get started!</h2>
      <ExpenseItem title={expenses[0].title} amount={expenses[0].amount} date={expenses[0].date}></ExpenseItem>
      <ExpenseItem title={expenses[1].title} amount={expenses[1].amount} date={expenses[1].date}></ExpenseItem>
      <ExpenseItem title={expenses[2].title} amount={expenses[2].amount} date={expenses[2].date}></ExpenseItem>
    </div>
  );
}

export default App;
```

