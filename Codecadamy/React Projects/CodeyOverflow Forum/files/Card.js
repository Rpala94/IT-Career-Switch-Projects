import React from 'react';
import Header from 'Header';
import Body from 'Body';

function Card(props) {
  return (
    <>
    <header profileImg = {props.commentObject.profileImg} username = 
    {props.commentObject.username} />
    <body comment ={props.commentObject.comment} />
    </>
  );
}

export default Card;