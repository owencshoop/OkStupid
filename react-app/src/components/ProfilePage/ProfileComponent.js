import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import SingleQuestionForm from "../auth/SingleQuestionForm";
import { discoverUserLoad } from "../../store/session";

export default function ProfilePage() {
    const user = useSelector((state) => state.session.user);
    const [loaded, setLoaded] = useState(false);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(discoverUserLoad())
        .then(() => setLoaded(true))
    }, [dispatch])

    if (!loaded) {
        return null;
    }

    return (
        <div>
            <h1>{user.username}'s Profile</h1>
            <img
                src={
                    user.userImages[0]
                        ? user.userImages[0].imageUrl
                        : "https://picsum.photos/256/256"
                }
                alt='profile-pic'
            />
            <h3>Name: {user.firstName}</h3>
            <p>Gender: {user.gender}</p>
            <p>Preferred Genders: {user.preferredGenders}</p>
            <p>
                Age range: {user.minAge} - {user.maxAge}
            </p>
            <p>Bio: {user.bio}</p>

            <div>
                <h4>Answer more questions</h4>
                <SingleQuestionForm />
            </div>
        </div>
    );
}
