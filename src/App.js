import React, {useState, useEffect} from 'react';
import './App.css';

const reqInit = {
  method : 'GET', 
  mode: 'cors', 
  // cache: 'default'
}

function InputForm(props) {
  const [name, setName] = useState('');
  const [nameError, setNameError] = useState('');
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState('');

  useEffect(() => {
    // TODO: name and email validation
    if (props.participants.map(p => p[0]).includes(name)) {
      setNameError('Error: Name must be unique!');
    } else {
      setNameError('')
    }
    if (props.participants.map(p => p[1]).includes(email)) {
      setEmailError('Error: E-mail address has already been used!');
    } else {
    }
  })

  return (
    <form onSubmit={event => { 
        setName(''); 
        setEmail(''); 
        props.handleSubmit(event, name, email);
    }}>
      <div>
      <label className='InputSection'>
        <div className='Input'>
          <>Name: </>
          <input type="text" value={name} onChange={e => setName(e.target.value)} />
        </div>
        <div className='Error'>{nameError}</div>
      </label>
      </div>
      <div>
      <label className='InputSection'>
        <div className='Input'>
          <>E-Mail: </>
          <input type="text" value={email} onChange={e => setEmail(e.target.value)} />
        </div>
        <p className='Error'>{emailError}</p>
      </label>
      </div>
      <input type="submit" value="Submit" />
    </form>
  )
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {participants: []};

    this.componentDidMount = this.componentDidMount.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.getParticipants = this.getParticipants.bind(this);
  }

  componentDidMount() {
    this.getParticipants()
  }

  getParticipants(qs=null) {
    var p = ''
    if (qs !== null) {
      let params = new URLSearchParams(qs);
      p = '?'+params.toString();
    }

    const req = new Request('http://localhost:5000/'+p, reqInit)
    console.log(req)

    fetch(req)
    .then( response => {
      console.log(response)
      if (response.status === 200) {
        return response.json();
      } else {
        throw new Error('Something went wrong on api server!');
      }
    })
    .then(json_data => {
      console.log(json_data)
      this.setState({participants: json_data[0]})
    });
  }

  handleSubmit(event, name, email) {
    // contact the server
    // this.setState({
    //   participants: this.state.participants.concat([[name, email]])
    // })
    this.getParticipants({'name':name, 'email':email})

    console.log(this.state.participants, name, email)
    event.preventDefault();
  }
  render() {
    const participants_list = this.state.participants.map((p) => {
      return(<li key={p[1]}>{p[0]} {p[1]}</li>)
    })
    return (
      <div className="App">
        <header className="App-header">
          <h1>Williams' Family Secret Santa Drawing</h1>
          <h3>Sign up:</h3>
          <InputForm participants={this.state.participants} handleSubmit={this.handleSubmit}/>
          <h3>Already signed up:</h3>
          <ul>{participants_list}</ul>
        </header>
      </div>
    );
  }
}

export default App;
