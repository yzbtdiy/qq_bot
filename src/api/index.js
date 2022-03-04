import requests from './request';

export const reqAnswers = questions =>
  requests({
    url: '/send_msg',
    method: 'get',
    params: {
      message_type: 'group',
      group_id: '755048599',
      message: questions
    }
  });
