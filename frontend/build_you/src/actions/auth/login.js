import { MAIN_URL } from "../../constants/apiUrls";

export function login_request(user_name, user_email) {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: 'React POST Request Example' })
        };
        fetch(MAIN_URL, requestOptions)
        .then(async response => {
            const data = await response.json();
            // check for error response
            if (!response.ok) {
                // get error message from body or default to response status
                const error = (data && data.message) || response.status;
                return Promise.reject(error);
            }
            return data.id;
        })
        .catch(error => {
            console.error('There was an error!', error);
            return error.toString();
        });
}