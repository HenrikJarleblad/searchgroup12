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
          message: "Hej, jag är en chatbot indexerad på en delmängd av Familjelivs data. Skriv en fråga så ska jag försöka hjälpa dig.",
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
    const question = this.state.value.trim()

    // do noting if no input
    if(question.length === 0){
      return
    }

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

    fetch('http://127.0.0.1:8000/?question=' + (question))
    .then((response) => {
      return response.json();
    })
    .then((myJson) => {

      if(myJson.confidence === 0){

        const newMessage = new Message({
          id: 1,
          message: "Jag är inte riktigt säker men:"
        });

        this.setState((prevState) => ({
          messages: [...prevState.messages, newMessage],
        }));

      }
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
              placeholder="Vad vill du veta?"
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
