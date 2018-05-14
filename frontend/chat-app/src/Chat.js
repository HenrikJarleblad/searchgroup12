'strict'
import { ChatFeed, Message } from 'react-chat-ui';
import React, { Component } from 'react';
import './Chat.css';

class Chat extends Component {
  constructor(props) {
    super()

    this.handleMessageSubmit = this.handleMessageSubmit.bind(this)
    this.handleMessageChange = this.handleMessageChange.bind(this)
    //this.askChatBot = this.askChatBot.bind(this)

    this.state = {
      is_typing: false,
      value: '',
      messages: [
        new Message({
          id: 1,
          message: "Hi, I'm FamBot. How can I help you?",
          senderName: "FamBot"
        })
      ]
    };
  }

  handleMessageChange(event){
    this.setState({value: event.target.value});
  }

  handleMessageSubmit(event){
    event.preventDefault();
    const question = this.state.value
    const newMessage = new Message({
      id: 0,
      message: question
    });
    this.setState((prevState) => ({
      messages: [...prevState.messages, newMessage],
      value:''
    }));
    this.askChatBot(question);

  }

  askChatBot(question){
    this.setState({
      is_typing: true
    });
    fetch('http://127.0.0.1:8000/')
    .then((response) => {
      return response.json();
    })
    .then((myJson) => {
      //console.log(myJson.answer);
      const newMessage = new Message({
        id: 1,
        message: myJson.answer
      });
      this.setState((prevState) => ({
        messages: [...prevState.messages, newMessage],
        is_typing: false
      }));
    });

  }

  render() {
    return(
      <div className="container">
        <div className="chat-wrapper">
          <ChatFeed
            messages={this.state.messages} // Boolean: list of message objects
            isTyping={this.state.is_typing} // Boolean: is the recipient typing
            showSenderName= {true}  // show the name of the user who sent the message
            bubblesCentered={true} //Boolean should the bubbles be centered in the feed?
            maxHeight={450}
          />
        <form onSubmit={this.handleMessageSubmit}>
            <input
              className="message-input"
              placeholder="What do you want to know?"
              type="text"
              value={this.state.value}
              onChange={this.handleMessageChange}
            />
          </form>
      </div>

      </div>


    );
  }
}

export default Chat;